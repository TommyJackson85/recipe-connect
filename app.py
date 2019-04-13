import os, json, ast, datetime
from flask import Flask, render_template, redirect, request, url_for, jsonify
from datetime import timedelta
from bson import json_util
from bson.son import SON
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import sys
print(sys.path)

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe-manager'
app.config["MONGO_URI"] = 'mongodb://bigtom98:funnybone98@ds131997.mlab.com:31997/recipe-manager'
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


mongo = PyMongo(app)   

#used to check if user is logged in and if it has foreign key of user id
@app.route('/')
def index():
    logbase = mongo.db.logbase.find_one({"data_type": "log"})
    print(logbase)
    logged_in=logbase['logged_in']
    if logged_in == True:
        user_id=logbase['user_id']
        return redirect(url_for('user_recipes', user_id=user_id))
    
    if logged_in == False:
        #initial boolean defaults on load
        login_exists = True 
        register_exists = False
        new_register = False
        return redirect(url_for('login_register',
                                login_exists=login_exists,
                                register_exists=register_exists,
                                new_register=new_register))
                                
@app.route('/login_register/<login_exists>/<register_exists>/<new_register>', methods=['POST', 'GET'])
def login_register(new_register, login_exists, register_exists):
        return render_template('login_register.html',
                                login_exists=login_exists,
                                register_exists=register_exists,
                                new_register=new_register)


#COME BACK AFTER FIXING foreign keys
@app.route('/logout_user', methods=['POST', 'GET'])
def logout_user():
    logbase = mongo.db.logbase.find_one({"data_type": "log"})
    logged_in=logbase['logged_in']
    login_exists = True
    register_exists = False
    new_register = False
    if logged_in == False:
        return redirect(url_for('login_register',
                        login_exists=login_exists,
                        register_exists=register_exists,
                        new_register=new_register))
    if logged_in == True:
        mongo.db.logbase.update({"data_type": "log"},
        {
            "data_type": "log",
            "logged_in": False,
            "user_id": ""
        })
        return redirect(url_for('login_register',
                                login_exists=login_exists,
                                register_exists=register_exists,
                                new_register=new_register))

@app.route('/register_user/', methods=['POST', 'GET'])
def register_user():
    users = mongo.db.users
    new_register = request.form.to_dict()
    print(mongo.db.users.find({ 'user_name': new_register['user_name']   }).count())
    if mongo.db.users.find({'user_name': new_register['user_name']}).count() > 0:
        new_register = True
        login_exists = True
        register_exists = True
        return redirect(url_for('login_register',
                                login_exists=login_exists,
                                register_exists=register_exists,
                                new_register=new_register))
    else:
        user_name = new_register["user_name"]
        user_country = new_register["user_country"]
        users.insert_one({
                "user_name":user_name,
                "user_country":user_country,
                "recipe_ids":[]
        })
        login_exists = True
        register_exists = False
        new_register = True
        return redirect(url_for('login_register',
                                login_exists=login_exists,
                                register_exists=register_exists,
                                new_register=new_register))
    

@app.route('/login_user', methods=['POST', 'GET'])
def login_user():
    posted_username = request.form.to_dict()
    if mongo.db.users.find({"user_name": posted_username["user_name"]}).count() == 0:
        new_register = False
        login_exists = False
        register_exists = False
        return redirect(url_for('login_register',
                        login_exists=login_exists,
                        register_exists=register_exists,
                        new_register=new_register))
    else:
        user = mongo.db.users.find_one({"user_name": posted_username["user_name"]})
        new_register = False
        login_exists = True
        register_exists = False
        #user = mongo.db.users.find_one({"user_name": posted_username["user_name"]})
        print(user["_id"])
        user_id = ObjectId(user["_id"])
        mongo.db.logbase.update( { "data_type": "log" }, 
        {       "logged_in": True,
                "data_type": "log",
                "user_id": ObjectId(user_id)
        })
        new_register = False
        return redirect(url_for('user_recipes',
                        user_id=user_id))
    
@app.route('/user_recipes/<user_id>')
def user_recipes(user_id):
    user=mongo.db.users.find_one({  "_id": ObjectId(user_id)     })
    recipe_ids = user['recipe_ids']
    if(len(recipe_ids) == 0):
            print(len(recipe_ids))
            return render_template("user_recipes.html",
                                    user_has_recipes=False,
                                    user_id=user_id,
                                    user=mongo.db.users.find_one({ "_id": ObjectId(user_id)     }),
                                    )
    if(len(recipe_ids) > 0):
            recipes=mongo.db.recipes.find({ '_id': {'$in': recipe_ids} })
            print(recipes)
            return render_template("user_recipes.html",
                                    user_has_recipes=True,
                                    user_id=user_id,
                                    user=mongo.db.users.find_one({ "_id": ObjectId(user_id)     }),
                                    recipes=recipes)
        
                            
@app.route('/add_recipe/<user_id>')
def add_recipe(user_id):
    return render_template("add_recipe.html", 
                            user_id=user_id,
                            user = mongo.db.users.find_one({  "_id": ObjectId(user_id)    }),
                            recipes=mongo.db.recipes.find())

@app.route('/insert_recipe/<user_id>', methods=['POST', 'GET'])
def insert_recipe(user_id):
    if request.method == 'POST':
        new_data= request.form.to_dict()
        user = mongo.db.users.find_one({  "_id": ObjectId(user_id)    })
        user_name = user["user_name"]
        user_country = user["user_country"]
        recipe_ingredients = json.loads(new_data['recipe_ingredients'])
        recipe_instructions = json.loads(new_data['recipe_instructions'])
        recipe_allergen_summary = json.loads(new_data['recipe_allergen_summary'])
        dt = datetime.datetime.now()
        
        recipe_id = mongo.db.recipes.insert(
        {       
                "user_id": ObjectId(user_id),
                "user_details": {
                    "name": user["user_name"],
                    "country": user["user_country"]
                },
                "recipe_name":new_data["recipe_name"],
                "recipe_cuisine":new_data["recipe_cuisine"],
                "recipe_description":new_data["recipe_description"],
                "recipe_ingredients":recipe_ingredients,
                "recipe_allergen_summary":recipe_allergen_summary,
                "recipe_instructions":recipe_instructions,
                "recipe_views":0,
                "recipe_upvotes":0,
                "last_modified": dt
        })
        print(recipe_id)
        mongo.db.users.update({'_id': ObjectId(user_id)}, 
            { '$push': { 'recipe_ids': recipe_id } }
        )
        return redirect(url_for('user_recipes',
                                user_id=user_id))

@app.route('/edit_recipe/<user_id>/<recipe_id>', methods=['GET'])
def edit_recipe(user_id, recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipe_id=the_recipe["_id"]
    recipe_name = the_recipe["recipe_name"]
    recipe_cuisine = the_recipe["recipe_cuisine"]
    recipe_description = the_recipe["recipe_description"]
    ingredients = json.dumps(the_recipe["recipe_ingredients"])
    instructions = json.dumps(the_recipe["recipe_instructions"])
    return render_template('edit_recipe.html', 
                            user_id=user_id,
                            user=mongo.db.users.find_one({  "_id": ObjectId(user_id)    }),
                            recipe_id=recipe_id,
                            recipe_name=recipe_name, 
                            recipe_cuisine=recipe_cuisine,
                            recipe_description=recipe_description, 
                            ingredients=ingredients, 
                            instructions=instructions)

@app.route('/update_recipe/<user_id>/<recipe_id>', methods=['POST', 'GET'])
def update_recipe(user_id, recipe_id):
    recipes = mongo.db.recipes
    edited_data = request.form.to_dict()
    recipe_instructions = json.loads(edited_data["recipe_instructions"])
    recipe_ingredients = json.loads(edited_data["recipe_ingredients"])
    recipe_allergen_summary = json.loads(edited_data["recipe_allergen_summary"])
    recipes.update( {'_id': ObjectId(recipe_id)},
        {   "$set":
                {
                    "recipe_name":edited_data["recipe_name"],
                    "recipe_cuisine":edited_data["recipe_cuisine"],
                    "recipe_description":edited_data["recipe_description"],
                    "recipe_ingredients":recipe_ingredients,
                    "recipe_allergen_summary":recipe_allergen_summary,
                    "recipe_instructions":recipe_instructions,
                    "last_modified": datetime.datetime.now()
                }
        })
    return redirect(url_for('user_recipes',
                            user_id=user_id))

@app.route('/delete_recipe/<user_id>/<recipe_id>', methods=['GET'])
def delete_recipe(user_id, recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    #pulls deleted recipe id from recipe creator's recipe_ids
    mongo.db.users.update({'_id': ObjectId(user_id)},
    { '$pull': { 'recipe_ids': ObjectId(recipe_id) } })
    
    #pulls deleted recipe id from users upvoted recipes, if they upvoted it recipe_ids
    mongo.db.users.update({'upvoted_recipes': ObjectId(user_id)},
    { '$pull': { 'upvoted_recipes': ObjectId(recipe_id) } })
    
    return redirect(url_for('user_recipes',
                            user_id=user_id))
"""                            
@app.route('/all_recipes/<user_id>/<recipes_found>/<query_object>', methods=['POST', 'GET'])
def all_recipes(user_id, recipes_found, query_object):
    #searchbase = mongo.db.logbase.find_one({"data_type": "search"})
    recipes=mongo.db.recipes.find(query_object).sort([("recipe_upvotes", 1), ("recipe_views", 1), ("last_modified", -1)] ).limit(4)
    print(query_object)
    return render_template("all_recipes.html",
                            user_id=user_id,
                            recipes=recipes,
                            recipes_found=recipes_found)
"""

@app.route('/search_recipes/<user_id>/<form_requested>', methods=['POST', 'GET'])
# shows all recipes and user can search, view and rate recipes
def search_recipes(user_id, form_requested):
    recipes_found = False #initial setting
    query_object = {}
    if form_requested == 'True':
        new_search = request.form.to_dict()
        print(new_search)
        if len(new_search["recipe_cuisine"]) > 0:
            query_object["recipe_cuisine"] = new_search["recipe_cuisine"]
        if len(new_search["recipe_ingredient"]) > 0:
            query_object["recipe_ingredients.ingredient"] = new_search["recipe_ingredient"]
        if len(new_search["recipe_allergen"]) > 0:      
            query_object["recipe_allergen_summary"] = { "$ne": new_search["recipe_allergen"]  }
            
        mongo.db.searchbase.update({"data_type": "search"}, { 
            "$set": {
                "cuisine":  new_search["recipe_cuisine"],
                "ingredient": new_search["recipe_ingredient"],
                "allergen": new_search["recipe_allergen"]           
            }
        })
    else:
        searchbase = mongo.db.searchbase.find_one({"data_type": "search"})
        if len(searchbase["cuisine"]) > 0:
            query_object["recipe_cuisine"] = searchbase["cuisine"]
        if len(searchbase["ingredient"]) > 0:
            query_object["recipe_ingredients.ingredient"] = searchbase["ingredient"]
            { "ingredient": searchbase["ingredient"] }
        if len(searchbase["allergen"]) > 0:
            query_object["recipe_allergen_summary"] = { "$ne": searchbase["allergen"]  }
    
    if mongo.db.recipes.find(query_object).count() > 0:
        recipes_found = True
        #recipes=mongo.db.recipes.find(query_object).sort([("recipe_upvotes", -1), ("recipe_views", -1), ("last_modified", -1)] ).limit(20)
        seven_days_before = datetime.datetime.now() - timedelta(days=3)
        print(mongo.db.recipes.find(query_object).count())
        recipes=mongo.db.recipes.find(query_object).sort([("recipe_upvotes", -1), ("recipe_views", -1), ("last_modified", -1)] ).limit(20)
        #print(list(recipes));
        #list(recipes).count({})
        return render_template("search_recipes.html",
                                seven_days_before = datetime.datetime.now() - timedelta(days=3),
                                user_id=user_id,
                                recipes_found=recipes_found,
                                searchbase = mongo.db.searchbase.find_one({"data_type": "search"}),
                                recipes=list(recipes))
    else:
        recipes_found = False
        return render_template("search_recipes.html",
                                user_id=user_id,
                                recipes_found=recipes_found,
                                searchbase = mongo.db.searchbase.find_one({"data_type": "search"}))

@app.route('/recipe/<recipe_id>/<user_id>/<upvoting>', methods=['POST', 'GET'])                                
def recipe(recipe_id, user_id, upvoting):
    if upvoting == 'True':
        #when user decides to upvote a recipe (from the individual recipe page) it reloads the page
        mongo.db.users.update({'_id': ObjectId(user_id)}, 
                { '$push': { 'upvoted_recipes': recipe_id } }
        )
        mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
                { "$inc": { "recipe_upvotes": 1 }   }        
        )
    else:
        #when a user opens a recipe page after searching on the search page
        mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
                { "$inc": { "recipe_views": 1 }   }        
        )
    if user_id == 'no_user':
        return render_template("recipe.html",
                                user_id=user_id,
                                recipe_id=recipe_id,
                                recipe = mongo.db.recipes.find_one({ "_id": ObjectId(recipe_id) })
                            )
    else:
        return render_template("recipe.html",
                                user_id=user_id,
                                recipe_id=recipe_id,
                                user = mongo.db.users.find_one({ "_id": ObjectId(user_id) }),
                                recipe = mongo.db.recipes.find_one({ "_id": ObjectId(recipe_id) })
                            )

#used this mongodb manual for reference when designing my aggregation query for the recipe_charts page
#https://docs.mongodb.com/manual/tutorial/aggregation-with-user-preference-data/
@app.route('/recipe_charts/<user_id>/<category>', methods=['POST', 'GET'])                                
def recipe_charts(user_id, category):
    query = []
    if category == "allergens":
        query.append({ "$unwind" : "$recipe_allergen_summary" })
        query.append({ "$group" : { "_id" : "$recipe_allergen_summary", "number" : { "$sum" : 1 } } })
        
    elif category == "cuisine":
        query.append({ "$group" : { "_id" : "$recipe_cuisine", "number" : { "$sum" : 1 } } })
    
    elif category == "ingredients":
        query.append({ "$unwind" : "$recipe_ingredients" })
        query.append({ "$group" : { "_id" : "$recipe_ingredients.ingredient", "number" : { "$sum" : 1 } } })
    
    elif category == "country":
         query.append({ "$group" : { "_id" : "$user_details.country", "number" : { "$sum" : 1 } } })
    
    #all categories require the following
    query.append({ "$sort" : { "number" : -1 } })
    query.append({ "$limit" : 5 })
    
    #retrieving and listing data and turning it into a string
    query_sum = mongo.db.recipes.aggregate(query)
    summary = json.dumps(list(query_sum))
    print(summary)
    
    return render_template("recipe_charts.html",
                            user_id=user_id,
                            summary=summary,
                            category=category)
    
if __name__ == '__main__':      
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)