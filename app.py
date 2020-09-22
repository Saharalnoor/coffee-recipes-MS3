import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'coffee_recipes'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html", page_title="Home")


@app.route("/view_recipe_category/<selected_category>")
def view_recipe_category(selected_category):
    all_recipes = mongo.db.recipes.find()
    return render_template("view_recipe_category.html",
                           recipes=all_recipes,
                           selected_category=selected_category,
                           page_title=selected_category + "Recipes")


@app.route("/recipe_details/<recipe_id>")
def recipe_details(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_details.html",
                           recipe=the_recipe,
                           page_title="Recipe Details")


@app.route("/add_recipes/")
def add_recipes():
    all_categories = mongo.db.categories.find()

    return render_template("add_recipes.html",
                           all_categories=all_categories,
                           page_title="Add Your Own Recipe")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
            port=int(os.environ.get('PORT')), debug=True)
