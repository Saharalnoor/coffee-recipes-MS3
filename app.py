import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGODB_NAME"] = 'coffee_recipes'
app.config["MONGO_URI"] = app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html", page_title="Home")

@app.route("/hot_coffee")
def hot_coffee():
    return render_template("hot_coffee.html", 
                            categories=mongo.db.categories.find())



@app.route("/iced_coffee")
def iced_coffee():
    return render_template("iced_coffee.html",
                            categories=mongo.db.categories.find())


@app.route("/add_recipes")
def add_recipes():
    all_categories = mongo.db.categories.find()
    return render_template("add_recipes.html",
                           categories=all_categories,
                           page_title="Add Your Own Recipe")




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
