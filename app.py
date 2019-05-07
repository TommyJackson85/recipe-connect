import os
import json
import ast
import datetime
import re
import sys
import urllib.request

from werkzeug.urls import url_parse
from flask import Flask, render_template, redirect, request, url_for, jsonify
from datetime import timedelta
from bson import json_util
from bson.son import SON
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

print(sys.path)

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe-manager'
app.config["MONGO_URI"] = 'mongodb://bigtom98:funnybone98@ds131997.mlab.com:31997/recipe-manager'
# app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

# used to check if user is logged in and if it has foreign key of user id
@app.route('/')
def index():
    logbase = mongo.db.logbase.find_one({"data_type": "log"})
    logged_in = logbase['logged_in']  # shows which user is logged in
    if logged_in is True:
        logged_user = mongo.db.users.find_one({"_id": ObjectId(logbase["user_id"])})
        return redirect(url_for('home',
                        user_id=logbase['user_id'],
                        user_name=logged_user["user_name"]))
    if logged_in is False:
        return redirect(url_for('home',
                        user_id="no_user",
                        user_name="no_user"))
    
    
@app.route('/home/<user_id>/<user_name>', methods=['POST', 'GET'])
def home(user_id, user_name):
    return render_template('home.html',
                           user_name=user_name,
                           user_id=user_id)
                               
                               
@app.route('/login_register/<login_exists>/<register_exists>/<new_register>', 
           methods=['POST', 'GET'])
def login_register(new_register, login_exists, register_exists):
        return render_template('login_register.html',
                               login_exists=login_exists,
                               register_exists=register_exists,
                               new_register=new_register)


# COME BACK AFTER FIXING foreign keys
@app.route('/logout_user', methods=['POST', 'GET'])
def logout_user():
    logbase = mongo.db.logbase.find_one({"data_type": "log"})
    logged_in = logbase['logged_in']
    if logged_in is False:
        # Unlikely log out link will appear. Only set incase of error
        return redirect(url_for('login_register',
                                login_exists=True,
                                register_exists=False,
                                new_register=False))
    if logged_in is True:
        mongo.db.logbase.update({"data_type": "log"},
                                {
                                    "data_type": "log",
                                    "logged_in": False,
                                    "user_id": ""
                                })
        return redirect(url_for('login_register',
                                login_exists=True,
                                register_exists=False,
                                new_register=False))


@app.route('/register_user/', methods=['POST', 'GET'])
def register_user():
    users = mongo.db.users
    new_register = request.form.to_dict()
    if mongo.db.users.find(
        {'user_name': new_register['user_name']}
    ).count() > 0:
        # if user name already exists, registration fails
        return redirect(url_for('login_register',
                                login_exists=True,
                                register_exists=True,
                                new_register=True))
    else:
        # if user name doesn't exist
        user_name = new_register["user_name"]
        user_country = new_register["user_country"]
        users.insert_one({
                "user_name": user_name,
                "user_country": user_country,
                "recipe_ids": []
        })
        return redirect(url_for('login_register',
                                login_exists=True,
                                register_exists=False,
                                new_register=True))
    

@app.route('/login_user', methods=['POST', 'GET'])
def login_user():
    posted_username = request.form.to_dict()
    if mongo.db.users.find(
        {"user_name": posted_username["user_name"]}
    ).count() == 0:
        # if username doesn't exist, login attempt fails
        return redirect(url_for('login_register',
                        login_exists=False,
                        register_exists=False,
                        new_register=False))
    else:
        # if username exists
        user = mongo.db.users.find_one(
            {"user_name": posted_username["user_name"]}
        )
        user_id = ObjectId(user["_id"])
        mongo.db.logbase.update({"data_type": "log"}, 
                                {"logged_in": True,
                                 "data_type": "log",
                                 "user_id": ObjectId(user_id)})
        return redirect(url_for('user_recipes',
                                user_id=user_id))

    
    
@app.route('/user_recipes/<user_id>')
def user_recipes(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    recipe_ids = user['recipe_ids']
    # recipe ids are foreign keys linking the users created recipes
    
    if(len(recipe_ids) == 0):
            return render_template("user_recipes.html",
                                   user_has_recipes=False,
                                   user_id=user_id,
                                   user=mongo.db.users.find_one(
                                       {"_id": ObjectId(user_id)}
                                   ))
                                 
    if(len(recipe_ids) > 0):
            recipes = mongo.db.recipes.find({'_id': {'$in': recipe_ids}})
            return render_template("user_recipes.html",
                                   user_has_recipes=True,
                                   user_id=user_id,
                                   user=user,
                                   recipes=list(recipes))
                                  
                            
@app.route('/add_recipe/<user_id>')
def add_recipe(user_id):
    return render_template("add_recipe.html", 
                           user_id=user_id,
                           user=mongo.db.users.find_one(
                               {"_id": ObjectId(user_id)}
                           ))


@app.route('/insert_recipe/<user_id>', methods=['POST', 'GET'])
def insert_recipe(user_id):
    if request.method == 'POST':
        new_data = request.form.to_dict()
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        user_name = user["user_name"]
        user_country = user["user_country"]
        recipe_ingredients = json.loads(new_data['recipe_ingredients'])
        recipe_instructions = json.loads(new_data['recipe_instructions'])
        recipe_allergen_summary = json.loads(
            new_data['recipe_allergen_summary']
        )
        
        #used if image url won't work
        default_image = "http://www.inimco.com/wp-content/themes/consultix/images/no-image-found-360x260.png"
        try:
            #tests image first
            test_image = new_data["recipe_image"]
            if url_parse(test_image).scheme:
                #data urls are excluded
                if url_parse(test_image).scheme == 'data':
                    recipe_image = default_image
                else:
                    #prevents 403 error
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
                    url_request = urllib.request.Request(test_image, headers = headers)
                    test = urllib.request.urlopen(url_request)
                    
                    #gets url type
                    url_type = test.info()['Content-type']
                    if url_type.endswith("png") or url_type.endswith("jpeg") or url_type.endswith("gif"):
                        recipe_image = new_data["recipe_image"]
                    else:
                        recipe_image = default_image
            else:
                print("not url")
                if not test_image:
                    #if user hasn't added to image field, 
                    #no image will display from templates, 
                    #images are ignored with empty strings
                    recipe_image = new_data["recipe_image"]
                else:
                    #if user created a faulty url, default image is used
                    recipe_image = default_image
        
        except Exception as e:
            #inform them that a general error has occurred
            pass
            recipe_image = default_image
        
        datetime_now = datetime.datetime.now()
        recipe_id = mongo.db.recipes.insert({       
                "user_id": ObjectId(user_id),
                "user_details": {
                    "name": user["user_name"],
                    "country": user["user_country"]
                },
                "recipe_name": new_data["recipe_name"],
                "recipe_cuisine": new_data["recipe_cuisine"],
                "recipe_description": new_data["recipe_description"],
                "recipe_image": recipe_image,
                "recipe_ingredients": recipe_ingredients,
                "recipe_allergen_summary": recipe_allergen_summary,
                "recipe_instructions": recipe_instructions,
                "recipe_views": 0,
                "recipe_upvotes": 0,
                "last_modified": datetime_now
        })
        mongo.db.users.update({'_id': ObjectId(user_id)}, 
                              {'$push': {'recipe_ids': recipe_id}})
        return redirect(url_for('user_recipes',
                                user_id=user_id))


@app.route('/edit_recipe/<user_id>/<recipe_id>', methods=['GET'])
def edit_recipe(user_id, recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # ingredients object and instructions array 
    # turned to string for easier passing to JavaScript JSON
    ingredients = json.dumps(the_recipe["recipe_ingredients"])
    instructions = json.dumps(the_recipe["recipe_instructions"])
    recipe_image = the_recipe["recipe_image"]
    
    return render_template('edit_recipe.html', 
                           user_id=user_id,
                           user=mongo.db.users.find_one(
                               {"_id": ObjectId(user_id)}
                           ),
                           recipe_id=the_recipe["_id"],
                           recipe_name=the_recipe["recipe_name"],
                           recipe_cuisine=the_recipe["recipe_cuisine"],
                           recipe_description=the_recipe["recipe_description"],
                           recipe_image=the_recipe["recipe_image"],
                           ingredients=ingredients, 
                           instructions=instructions)


@app.route('/update_recipe/<user_id>/<recipe_id>', methods=['POST', 'GET'])
def update_recipe(user_id, recipe_id):
    
    edited_data = request.form.to_dict()
    recipe_instructions = json.loads(edited_data["recipe_instructions"])
    recipe_ingredients = json.loads(edited_data["recipe_ingredients"])
    recipe_allergen_summary = json.loads(
        edited_data["recipe_allergen_summary"]
    )
    
    #used if image url won't work
    default_image = "http://www.inimco.com/wp-content/themes/consultix/images/no-image-found-360x260.png"
    try:
        #tests image first
        test_image = edited_data["recipe_image"]
        if url_parse(test_image).scheme:
            #data urls are excluded
            if url_parse(test_image).scheme == 'data':
                recipe_image = default_image
            else:
                #prevents 403 error
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
                url_request = urllib.request.Request(test_image, headers = headers)
                test = urllib.request.urlopen(url_request)
                
                #gets url type
                url_type = test.info()['Content-type']
                if url_type.endswith("png") or url_type.endswith("jpeg") or url_type.endswith("gif"):
                    recipe_image = edited_data["recipe_image"]
                else:
                    recipe_image = default_image
        else:
            if not test_image:
                #if user hasn't added to image field, 
                #no image will display from templates, 
                #images are ignored with empty strings
                recipe_image = edited_data["recipe_image"]
            else:
                #if user created a faulty url, default image is used
                recipe_image = default_image
    
    except Exception as e:
        #inform them that a general error has occurred
        pass
        recipe_image = default_image
    
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
                            {"$set":
                                {"recipe_name": edited_data["recipe_name"],
                                 "recipe_cuisine":
                                     edited_data["recipe_cuisine"],
                                 "recipe_description":
                                     edited_data["recipe_description"],
                                 "recipe_image": recipe_image,
                                 "recipe_ingredients": recipe_ingredients,
                                 "recipe_allergen_summary":
                                     recipe_allergen_summary,
                                 "recipe_instructions": recipe_instructions,
                                 "last_modified": datetime.datetime.now()}})
    return redirect(url_for('user_recipes',
                            user_id=user_id))
                            

@app.route('/delete_recipe/<user_id>/<recipe_id>', methods=['GET'])
def delete_recipe(user_id, recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    # pulls deleted recipe id from recipe creator's recipe_ids
    mongo.db.users.update({'_id': ObjectId(user_id)},
                          {'$pull': {'recipe_ids': ObjectId(recipe_id)}})
    # finds users who upvoted the recipe, 
    # and the removes the recipe's foreign 
    # key from users upvoted recipes
    users_upvoting = mongo.db.users.find({'upvoted_recipes': recipe_id})
    user_list = (list(users_upvoting))
    # For loop is temporary. Looking for alternative update 
    # method to update multipe objects on one request.
    for i in range(len(user_list)):
        mongo.db.users.update({'_id': ObjectId(user_list[i]['_id'])},
                              {'$pull': {'upvoted_recipes': recipe_id}})
    return redirect(url_for('user_recipes',
                            user_id=user_id))


@app.route('/search_recipes/<user_id>/<form_requested>', 
           methods=['POST', 'GET'])
def search_recipes(user_id, form_requested):
    recipes_found = False  # initial setting
    query_object = {}  # initial setting
    if form_requested == 'True':
        # if user clicks search button on the search form
        new_search = request.form.to_dict()
        # builds object from the query input values. 
        # The query is not strict and is case insensitive,
        # for more varied results
        if len(new_search["recipe_cuisine"]) > 0:
            query_object["recipe_cuisine"] = {"$regex": 
                                              new_search["recipe_cuisine"], 
                                              '$options': 'i'}        
        if len(new_search["recipe_ingredient"]) > 0:
            query_object["recipe_ingredients.ingredient"] = {'$regex': new_search['recipe_ingredient'], 
                                                             '$options': 'i'}           
        if len(new_search["recipe_allergen"]) > 0:      
            query_object["recipe_allergen_summary"] = {"$not": re.compile(new_search["recipe_allergen"], re.IGNORECASE)}
        
        # searchbase collection is just one object 
        # for updating the last search query
        mongo.db.searchbase.update({"data_type": "search"}, { 
            "$set": {
                "cuisine":  new_search["recipe_cuisine"],
                "ingredient": new_search["recipe_ingredient"],
                "allergen": new_search["recipe_allergen"]           
            }
        })
    else:
        # if loading search page from a link it reloads last search results
        searchbase = mongo.db.searchbase.find_one({"data_type": "search"})
        if len(searchbase['cuisine']) > 0:
            query_object["recipe_cuisine"] = {'$regex': searchbase['cuisine'], 
                                              '$options': 'i'}
        if len(searchbase['ingredient']) > 0:                   
            query_object['recipe_ingredients.ingredient'] = {'$regex': searchbase['ingredient'], '$options': 'i'}
        if len(searchbase['allergen']) > 0:              
            query_object['recipe_allergen_summary'] = {'$not': re.compile(searchbase['allergen'], re.IGNORECASE)}
    
    # search attempt. checks number count first
    if mongo.db.recipes.find(query_object).count() > 0:
        recipes_found = True
        seven_days_before = datetime.datetime.now() - timedelta(days=7)
        recipes = mongo.db.recipes.find(query_object).sort(
            [("recipe_upvotes", -1),
             ("recipe_views", -1), 
             ("last_modified", -1)]
        ).limit(20)
        seven_days_before = datetime.datetime.now() - timedelta(days=7)
        return render_template("search_recipes.html",
                               seven_days_before=seven_days_before,
                               user_id=user_id,
                               recipes_found=recipes_found,
                               searchbase=mongo.db.searchbase.find_one(
                                   {"data_type": "search"}
                               ),
                               recipes=list(recipes))
    else:
        recipes_found = False
        return render_template("search_recipes.html",
                               user_id=user_id,
                               recipes_found=recipes_found,
                               searchbase=mongo.db.searchbase.find_one(
                                   {"data_type": "search"}))


@app.route('/recipe/<recipe_id>/<user_id>/<upvoting>', methods=['POST', 'GET'])                                
def recipe(recipe_id, user_id, upvoting):
    if upvoting == 'True':
        # when user decides to upvote a recipe 
        # (from the individual recipe page), it reloads page
        # adds recipe foreign key to user database
        mongo.db.users.update({'_id': ObjectId(user_id)}, 
                              {'$push': {'upvoted_recipes': recipe_id}})
      
        mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
                                {"$inc": {"recipe_upvotes": 1}})
    else:
        # when a user opens a recipe page after searching on the search page
        mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
                                {"$inc": {"recipe_views": 1}})
        
    if user_id == 'no_user':
        # if no user logged in
        return render_template("recipe.html",
                               user_id=user_id,
                               recipe_id=recipe_id,
                               recipe=mongo.db.recipes.find_one(
                                   {"_id": ObjectId(recipe_id)}
                               ))
    else:
        return render_template("recipe.html",
                               user_id=user_id,
                               recipe_id=recipe_id,
                               user=mongo.db.users.find_one(
                                   {"_id": ObjectId(user_id)}),
                               recipe=mongo.db.recipes.find_one(
                                   {"_id": ObjectId(recipe_id)}))


# used this mongodb manual for reference when 
@app.route('/recipe_charts/<user_id>/<category>', methods=['POST', 'GET'])                                
def recipe_charts(user_id, category):
    query = []
    if category == "allergens":
        query.append({"$unwind": "$recipe_allergen_summary"})
        query.append({"$group": {"_id": "$recipe_allergen_summary", 
                                 "number": {"$sum": 1}}})
        
    elif category == "cuisine":
        query.append({"$group": {"_id": "$recipe_cuisine", 
                                 "number": {"$sum": 1}}})
    
    elif category == "ingredients":
        query.append({"$unwind": "$recipe_ingredients"})
        query.append({"$group": {"_id": "$recipe_ingredients.ingredient", 
                                 "number": {"$sum": 1}}})
    
    elif category == "country":
        query.append({"$group": {"_id": "$user_details.country", 
                                 "number": {"$sum": 1}}})

    # for all categories
    query.append({"$sort": {"number": -1}})
    query.append({"$limit": 5})
    
    # retrieving and listing data and turning it into a string
    query_sum = mongo.db.recipes.aggregate(query)
    summary = json.dumps(list(query_sum))
    return render_template("recipe_charts.html",
                           user_id=user_id,
                           summary=summary,
                           category=category)
    
if __name__ == '__main__':      
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)