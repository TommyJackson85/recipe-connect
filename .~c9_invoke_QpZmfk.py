import os, json, ast
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe-manager'
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["MONGO_URI"] = 'mongodb://bigtom98:funnybone98@ds131997.mlab.com:31997/recipe-manager'

mongo = PyMongo(app)
#print(mongo.db.recipes.find())

logged_in = False

@app.route('/')
@app.route('/login_register', methods=['POST', 'GET'])
def login_register():
    return render_template('login_register.html',
                            recipes=mongo.db.recipes.find())
                            
@app.route('/user_recipes')
def user_recipes():
    return render_template("user_recipes.html", 
                            recipes=mongo.db.recipes.find())
                            
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", 
                            recipes=mongo.db.recipes.find()) 
                            
@app.route('/insert_recipe',methods=["GET", "POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    if request.method == 'POST':
        #a = request.get_json()
        recipe_name = request.form["recipe_name"]
        #d = json.loads(json.dumps(a))
        #print("a is:")
        #print(a)
        #print("d is:")
        print(recipe_)
        #recipes.insert(d)
        return redirect(url_for('user_recipes'))


@app.route('/search_recipes')
# shows all recipes and user can search, view and rate recipes
def search_recipe():
    return render_template("search_recipes.html", 
                            recipes=mongo.db.recipes.find()) 
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=F)