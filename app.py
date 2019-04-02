import os, json, ast
from flask import Flask, render_template, redirect, request, url_for, jsonify

from bson import json_util
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import sys
print(sys.path)

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe-manager'
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["MONGO_URI"] = 'mongodb://bigtom98:funnybone98@ds131997.mlab.com:31997/recipe-manager'

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
                            user=mongo.db.users.find_one({  "_id": ObjectId(user_id)    }),
                            recipes=mongo.db.recipes.find())

@app.route('/insert_recipe/<user_id>', methods=['POST', 'GET'])
def insert_recipe(user_id):
    if request.method == 'POST':
        #new_data = request.get_json()
        new_data= request.form.to_dict()

        recipe_ingredients = json.loads(new_data['recipe_ingredients'])
        recipe_instructions = json.loads(new_data['recipe_instructions'])
        
        recipe_id = mongo.db.recipes.insert(
        {       
                "user_id": ObjectId(user_id),
                "recipe_name":new_data["recipe_name"],
                "recipe_cuisine":new_data["recipe_cuisine"],
                "recipe_description":new_data["recipe_description"],
                "recipe_ingredients":recipe_ingredients,
                "recipe_instructions":recipe_instructions,
                "recipe_views":0,
                "recipe_upvotes":0
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
    recipes.update( {'_id': ObjectId(recipe_id)}, 
        {   "$set":
                {
                    "recipe_name":edited_data["recipe_name"],
                    "recipe_cuisine":edited_data["recipe_cuisine"],
                    "recipe_description":edited_data["recipe_description"],
                    "recipe_ingredients":recipe_ingredients,
                    "recipe_instructions":recipe_instructions
                }
        })
    return redirect(url_for('user_recipes',
                            user_id=user_id))

@app.route('/delete_recipe/<user_id>/<recipe_id>', methods=['GET'])
def delete_recipe(user_id, recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    mongo.db.users.update({'_id': ObjectId(user_id)},
    { '$pull': { 'recipe_ids': ObjectId(recipe_id) } })
    return redirect(url_for('user_recipes',
                            user_id=user_id))


@app.route('/search_recipes')
# shows all recipes and user can search, view and rate recipes
def search_recipe():
    return render_template("search_recipes.html", 
                            recipes=mongo.db.recipes.find()) 
if __name__ == '__main__':      
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)