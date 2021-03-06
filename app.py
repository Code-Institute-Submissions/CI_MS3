import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Index page
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# All recipes page
@app.route("/all_recipes")
def all_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# Recipes by category, solution by MatthewYong on Github
@app.route("/recipes_by_category/<category>")
def recipes_by_category(category):
    category_current = {"category_name": category}
    name = mongo.db.recipes.find_one(category_current)
    recipes = mongo.db.recipes.find(category_current)
    return render_template(
        "recipes_by_category.html", recipes=recipes, name=name)


# Page for each individual recipe
@app.route("/get_recipe/<recipe_id>")
def get_recipe(recipe_id):
    single_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if single_recipe:
        return render_template("get_recipe.html", recipe=single_recipe)
    # If page for recipe is not found
    else:
        return render_template("404.html")


# The signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # If username already exists:
        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("signup"))
        # Recover requested details and hash password, insert into database
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        # On successful signup
        session["user"] = request.form.get("username").lower()
        flash("Signup Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")


# Log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # On successful login
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            # If username or password don't match
            else:
                flash("Incorrect username, password or both!")
                return redirect(url_for("login"))
        # If username is not found
        else:
            flash("Incorrect username, password or both!")
            return redirect(url_for("login"))

    return render_template("login.html")


# Profile page, also lists recipes added by current user on the page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Solution for listing recipes by a given user by MatthewYong on Github
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    current_user = {"added_by": username}
    recipes = mongo.db.recipes.find(current_user)
    if session["user"]:
        return render_template(
            "profile.html", username=username, user_recipes=recipes)

    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    flash("You logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# Add new recipe
@app.route("/new_recipe", methods=["GET", "POST"])
def new_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_description": request.form.get("recipe_description"),
            "servings": request.form.get("servings"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.getlist("ingredients"),
            "instructions": request.form.getlist("instructions"),
            "recipe_image": request.form.get("recipe_image"),
            "added_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added!")
        return redirect(url_for("all_recipes"))

    categories = mongo.db.categories.find()
    return render_template("new_recipe.html", categories=categories)


# Edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        edit = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_description": request.form.get("recipe_description"),
            "servings": request.form.get("servings"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.getlist("ingredients"),
            "instructions": request.form.getlist("instructions"),
            "recipe_image": request.form.get("recipe_image"),
            "added_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe updated!")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# Delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted!")
    return redirect(url_for("all_recipes"))


# Error pages, 404 & 500
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
