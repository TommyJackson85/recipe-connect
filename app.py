import os, json, ast, requests
from flask import Flask, render_template, redirect, request, url_for, jsonify

from bson import json_util
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import sys
print(sys.path)


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe-manager'
app.config["MONGO_URI"] = os.getenv('MONGOURI')
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
        return redirect(url_for('login_register'))
    
#COME BACK AFTER FIXING foreign keys
@app.route('/logout_user', methods=['POST', 'GET'])
def logout_user():
    logbase = mongo.db.logbase.find_one({"data_type": "log"})
    logged_in=logbase['logged_in']
    if logged_in == False:
        return redirect('login_register')
    if logged_in == True:
        mongo.db.logbase.update({"data_type": "log"},
        {
            "data_type": "log",
            "logged_in": False,
            "user_id": ""
        })
        return redirect(url_for('login_register'))

@app.route('/login_register', methods=['POST', 'GET'])
def login_register():
        return render_template('login_register.html')

@app.route('/register_user', methods=['POST', 'GET'])
def register_user():
    users = mongo.db.users
    new_register = request.form.to_dict()
    user_name = new_register["user_name"]
    user_country = new_register["user_country"]
    #print(user)
    users.insert_one({
            "user_name":user_name,
            "user_country":user_country
    })
    #print(new_register)
    return redirect(url_for('login_register'))
    

@app.route('/login_user', methods=['POST', 'GET'])
def login_user():
    posted_username = request.form.to_dict()
    user = mongo.db.users.find_one({"user_name": posted_username["user_name"]})
    print(user["_id"])
    user_id = ObjectId(user["_id"])
    mongo.db.logbase.update( { "data_type": "log" }, 
    {       "logged_in": True,
            "data_type": "log",
            "user_id": ObjectId(user_id)
    })
    return redirect(url_for('user_recipes',
                    user_id=user_id))
    
@app.route('/user_recipes/<user_id>')
def user_recipes(user_id):
    return render_template("user_recipes.html", 
                            user_id=user_id,
                            user=mongo.db.users.find_one({ "_id": ObjectId(user_id)     }),
                            recipes=mongo.db.recipes.find({ "user_id": ObjectId(user_id)    })
                            )
                            
@app.route('/add_recipe/<user_id>')
def add_recipe(user_id):
    return render_template("add_recipe.html", 
                            user_id=user_id,
                            user=mongo.db.users.find_one({  "_id": ObjectId(user_id)    }),
                            recipes=mongo.db.recipes.find() 
                            )

@app.route('/insert_recipe/<user_id>', methods=['POST', 'GET'])
def insert_recipe(user_id):
    if request.method == 'POST':
        new_data = request.get_json()
        mongo.db.recipes.insert_one(
        {       
                "user_id": ObjectId(user_id),
                "recipe_name":new_data["recipe_name"],
                "recipe_cuisine":new_data["recipe_cuisine"],
                "recipe_description":new_data["recipe_description"],
                "recipe_ingredients":new_data["recipe_ingredients"],
                "recipe_instructions":new_data["recipe_instructions"],
                "recipe_views":new_data["recipe_views"],
                "recipe_upvotes":new_data["recipe_upvotes"]
        })            
        return redirect(url_for('user_recipes',
                                user_id=user_id))
 
        """
        next_page = url_for('user_recipes',
                            _external=True,
                            _scheme='https')

        return redirect(next_page, code=302)
        """

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
    edited_data = request.get_json()
    recipes.update( {'_id': ObjectId(recipe_id)}, 
    {
            "user_id": ObjectId(user_id),
            "recipe_name":edited_data["recipe_name"],
            "recipe_cuisine":edited_data["recipe_cuisine"],
            "recipe_description":edited_data["recipe_description"],
            "recipe_ingredients":edited_data["recipe_ingredients"],
            "recipe_instructions":edited_data["recipe_instructions"],
            "recipe_views":edited_data["recipe_views"],
            "recipe_upvotes":edited_data["recipe_upvotes"]
    })
    return redirect(url_for('user_recipes',
                            user_id=user_id))

@app.route('/delete_recipe/<user_id>/<recipe_id>', methods=['GET'])
def delete_recipe(user_id, recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('user_recipes',
                            user_id=user_id))


@app.route('/search_recipes')
# shows all recipes and user can search, view and rate recipes
def search_recipe():
    return render_template("search_recipes.html", 
                            recipes=mongo.db.recipes.find()) 
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)