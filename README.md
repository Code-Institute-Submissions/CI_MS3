# The Donnybrook Cookbook Website

This is a recipe site intended for sharing recipes, with a focus on Irish cuisine
but other dishes being allowed as well. Anyone can view any of the recipes, but to
make full use of the site’s functionality making a user account is required. Users
can create, edit and delete their own recipes in addition to viewing ones uploaded
by others. Each recipe contains an ingredients list, instructions list, how long it
takes to prepare the dish and how many servings it contains. The recipes also
contain an image of the dish.

** **

## UX

#### User stories
**As a first time visitor:**

* It's immediately clear to me what the purpose of the site is.
* I can browse recipes uploaded by others.
* I can look for recipes that best suit what I'm currently looking for by viewing
them by category.
* I can create an account.

**As a returning visitor:**
* I can log in.
* I can upload my own recipes.
* I can view recipes I have uploaded.
* I can edit my own recipes.
* I can delete my own recipes.

** **

## Database Structure

The project utilizes [MongoDB](https://www.mongodb.com) for the creation of a database. The database 'cookbook' is structured into three collections:

![Database schema](https://github.com/ssruoh/CI_MS3/blob/master/static/images/db-schema.PNG)

Below are examples of entries in each collection:

[categories](https://github.com/ssruoh/CI_MS3/blob/master/static/images/db-categories-image.PNG)

[recipes](https://github.com/ssruoh/CI_MS3/blob/master/static/images/db-recipes-image.PNG)

[users](https://github.com/ssruoh/CI_MS3/blob/master/static/images/db-users-image.PNG)

** **

## Design

**Color Scheme**

The site primarily focuses on Irish cuisine, so a color scheme matching the colors of
the Irish flag was chosen. This is engaging and convenient, since the colors of the
flag are also generally suitable for a cooking-related site for their warmth.

**Typography**

The fonts used for the site are Bad Script and Noto Sans. The Bad script fallback 
font is cursive, and for Noto Sans the fallback is sans-serif. Bad Script is used
as the font for headings and other text that should be particularly eye-catching, 
and Noto Sans is used as the standard font for bulk content for its clarity.

**Imagery**

The site contains many images of dishes, in accordance with the purpose of the site
to showcase the recipes they represent.

** **

## Wireframes

Preliminary [wireframes](https://github.com/ssruoh/CI_MS3/blob/master/The%20Donnybrook%20Cookbook%20Wireframes.pdf) were drafted in MS Paint prior to development.

** **

## Features

* Responsive on all screen sizes.
* Each page includes a navigation bar.
* Each page includes a footer with copyright information and social media links.
* The landing page includes a short explanation of the site's purpose, as well as links to recipes sorted by their category. There are also links to sign up or log in to the site.
* The Sign up page contains a form that lets users register an account.
* The Log in page contains a form that allows users to log in to their account.
* Users who log in gain access to the New Recipe link. This page includes a form that allows users to submit their own recipes to the site.
* Users who log in gain access to the Profile link. This page allows users to view, edit and delete recipes they have uploaded.

**Features To Implement**

* Ratings & Comments - It would be a helpful and nice feature if users could rate the recipes and comment on them.
* Images - Ideally, image submission should happen through uploading the files themselves rather than entering a URL due potential issues with images hosted elsewhere.
* More detailed userpages - The site is ‘communal’ in a way and it would be a beneficial feature if users could upload an image of themselves and perhaps an About section where they can write a bit about themselves and their particular interests related to cooking.
* Following users - A feature to allow users to follow others and get notifications about recipes added.
* A search functionality for keywords to help people find what they want once the collection size increased.

** **

## Languages used

* HTML5
* CSS3
* JavaScript
* Python
* Jinja

## Frameworks, Libraries & programs

1. Materialize 1.0.0
* Used for responsive site styling.
2. Flask
* The web framework used for building the application.
3. MongoDB
* The service used to store the data necessary for building the site.
4. JQuery
* JavaScript Library used primarily for enhanced Materialize functionality
5. Google Fonts
* Used to source the fonts used for the site.
6. Font Awesome
* Used for a few of its icons, such as the social media icons and the minus sign for deleting an input field.
7. Git
* Used for version control during development.
8. Github
* The code hosting platform for this project.

** **

## Testing

**Tools**

W3C Markup Validator was used to validate the HTML code. [Results]()

W3C CSS Validator was used to validate the CSS code. [Results]()

JSHint was used to validate the JavaScript code. [Results]()

PEP8 Online was used to validate the Python code. [Results]()

**Manual**

* Checked that there are no prominent issues with overflow or clipping on any of the pages.
* Checked that users who are not logged in have access only to landing page, all recipes, categories, log in and sign up pages in navigation.
* Checked that all recipes page displays all recipes, recipe pages by category display recipes for the category and that get_recipe displays a single recipe.
* Checked that sign up and login pages work properly: sign up/log in when conditions are met, error messages are displayed when a condition is not met.
* Checked that logged in users gain access to new recipe, profile, edit recipe and login pages.
* Checked that log out logs user out.
* Checked that profile page displays correct username and recipe cards for recipes added by that user, along with edit/delete buttons. Ensured the buttons work.
* Checked that alternate header and text is shown with jinja when viewing a profile that has not added any recipes.
* Checked that form for new recipe requires all fields and submits the recipe to the database.
* Checked that edit recipe button directs to page to edit recipe, and that edits are saved for that recipe.
* Checked that delete recipe deletes the recipe.
* Checked that trying to access a page for a recipe that has been deleted returns a 404 page.

**Known Issues**

* Images in cards are sometimes subject to issues such as stretching and cropping.

** **

## Deployment

Github and Heroku were utilized to deploy the project. The database was created with MongoDB.

**MongoDB**

1. Create an account on MongoDB
2. Create a new database by navigating to Clusters, then Collections, and clicking Create Database and filling in the desired details
3. Create the following collections
* categories
* recipes
* users
4. Assign the appropriate keys and values to the items. See above for the structure of each collection.

**Forking The Repository**

The copy of the Github repository can be forked to another account for viewing or editing without affecting the original one with the following steps:

1. Login to Github and locate the [repository](https://github.com/ssruoh/CI_MS3)
2. On top right, right under the Account menu and Notifications, click on the Fork button. This will create a copy of the repository to your Github account.

**Creating A Local Clone**

1. Login to Github and locate the [repository](https://github.com/ssruoh/CI_MS3)
2. Click on the green Code button
3. Click on the clipboard icon under "Clone with HTTPS" to copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the clone to be created.
6. Type `git clone` and paste the URL you copied from the clipboard:

```
$ git clone https://github.com/ssruoh/CI_MS3
```

7. Press Enter to create a local clone.

```
$ git clone https://github.com/ssruoh/CI_MS3
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

**Setting up the environment variables**


1. Start up Gitpod workspace. Create app.py file
2. Create .gitignore file
3. Create env.py file
4. Add env.py and __pycache__/ to .gitignore as files to not push
5. In Gitpod, install flask with `pip3 install flask`
6. In Gitpod, get flask and MongoDB to communicate: install flask_pymongo with `pip3 install flask_pymongo`
7. In Gitpod, install dnspython with `pip3 install dnspython` to use srv connection string
8. In env.py, import os and set up your environment variables thusly:

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "YOUR-SECRET-KEY")
os.environ.setdefault("MONGO_URI", "mongodb+srv://root:<your-password>@myfirstcluster.hgwqn.mongodb.net/<your-database-name>?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "YOUR-DATABASE-NAME")
```

9. Add Imports in app.py. ObjectId is imported so you can render ObjectId’s of items from MongoDB.

```
import os
from flask import Flask
from flask_pymongo import Pymongo
from bson.objectid import ObjectId.
if os.path.exists(“env.py”):
	import env
```

10. Create instance of flask in app.py:

```
app = Flask(__name__)
```

11. Provide the app the details as to where to run it in app.py:

```
if __name__ = “__main__”:
	app.run(host.os.environ.get(“IP”),
	port=int(os.environ.get(“PORT”)),
	debug=True)
```

**Heroku**

1. Set up files necessary for Heroku to run the app. Create a file with a list of dependencies: `pip3 freeze --local > requirements.txt`
2. Create Procfile with `echo web: python app.py > Procfile`
3. Go to Heroku, Create account and on the dashboard, click “New” in the dropdown and select “Create new app”
4. Input App name and select the region closest to you and click “Create app”
5. For this project, the method selected for deployment was automatic Github deployments. In the Deploy tab, Select “Github” under “Deployment method”
6. Under Connect to Github, ensure your Github profile is selected, and Search for the Github repository prepared for Heroku deployment.
7. Once the repository is found, click “Connect”
8. Provide Heroku the environment variables. Under Settings tab, click Reveal Config Vars and input the key - value variables as they are set up in the env.py file.
9. Back in the Deploy tab, scroll to Automatic Deploys and click “Enable Automatic Deploys”
10. Under Manual Deploy, click “Deploy Branch”. This process will take a few moments and if successful, you will get a message stating “Your app was successfully deployed.”

** **

## Testing User Requirements In UX Section

**First time visitors**

> It's immediately clear to me what the purpose of the site is.
* The landing page of the site has a large callout explaining the purpose of the site, and it also prompts newcomers to sign up to the site.

> I can browse recipes uploaded by others.
* The landing page and navigation bar contain links to all recipes.

> I can look for recipes that best suit what I'm currently looking for by viewing
them by category.
* The landing page and navigation bar contain links to recipes sorted by their category.

> I can create an account.
* Newcomers are instructed to sign up to the site on the landing page, and there is a link in the navigation bar to do the same if users aren't signed in.

**Returning visitors:**
> I can log in.
* The navigation bar has a link to form that allows users to log in.

> I can upload my own recipes.
* There is a link in the navigation bar for users to add New Recipe. On the Profile page, users who have not yet added recipes are also encouraged to get started and provided a link to the New Recipe page as well.

> I can view recipes I have uploaded.
* On the Profile page where users land as they sign in, the recipes added by the user are listed.

> I can edit my own recipes.
* On the profile page, the recipe cards for recipes added by the user contain an Edit button.

> I can delete my own recipes.
* On the profile page, the recipe cards for recipes added by the user contain a Delete button.

** **

## Credits

**Code**

The code for this project is largely based on the lessons provided by [Code Institute](https://codeinstitute.net/), the Python in particular.

[This Github issue post solution](https://github.com/Dogfalo/materialize/issues/1000) was adapted to stop the navbar brand logo from clipping out on smaller screen sizes.

[This Stack Overflow solution](https://stackoverflow.com/questions/37194886/does-materialize-css-framework-have-a-container-fluid-equivalent) was used to achieve full-width hero image background.

[This Stack Overflow solution](https://stackoverflow.com/questions/42884750/how-to-create-inline-lists-in-materializecss) was used to create a Bootstrap-like inline list for social links in the footer.

[This Stack Overflow solution](https://stackoverflow.com/questions/37127123/change-color-of-underline-input-and-label-in-materialize-css-framework) was used to change the input and label colors for forms.

[This Stack Overflow post](https://stackoverflow.com/questions/36458482/how-to-not-render-a-entire-string-with-jinja2) was used for inspiration as to how to truncate recipe descriptions in cards to avoid overflow.

[The JQuery method used in this Code Institute project by deevdz](https://github.com/Code-Institute-Submissions/deevdz-milestone-project-3) was adapted to dynamically add and delete input fields for add and edit recipe forms.

**Content**

This readme is similar in structure and language to the readme files of my previous projects. Inspiration for some sections and testing was drawn from the Code Institute projects of [deevdz](https://github.com/Code-Institute-Submissions/deevdz-milestone-project-3) and [MatthewYong](https://github.com/MatthewYong/recipes-connected)

Site content such as callout, headings and the like were written by the developer.

The recipes added to the site during development are from [allrecipes.com](https://www.allrecipes.com), [delish.com](https://www.delish.com) and [bbcgoodfood.com](https://www.bbcgoodfood.com/recipes/collection/irish-recipes). The same sites were used for inspiration for page layout and database structure.

**Media**

Images used during development are sourced from [allrecipes.com](https://www.allrecipes.com), [delish.com](https://www.delish.com), [bbcgoodfood.com](https://www.bbcgoodfood.com/recipes/collection/irish-recipes) or [Google Images](https://www.google.com/imghp?hl=en)

**Acknowledgments**

My Code Institute Mentor for helpful feedback and ideas.

The Code Institute Tutors for their support.

My friends for help with testing the site.
