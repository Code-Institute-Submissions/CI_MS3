# The Donnybrook Cookbook Website

This is a recipe site intended for sharing recipes, with a focus on Irish cuisine
but other dishes being allowed as well. Anyone can view any of the recipes, but to
make full use of the site’s functionality making a user account is required. Users
can create, edit and delete their own recipes in addition to viewing ones uploaded
by others. Each recipe contains an ingredients list, instructions list, how long it
takes to prepare the dish and how many servings it contains. The recipes also
contain an image of the dish.

## UX

#### User stories
**As a user:**

* It's immediately clear to me what the purpose of the site is.
* I can browse recipes uploaded by others.
* I can create an account.
* I can log in.
* I can upload my own recipes.
* I can look for recipes that best suit what I'm currently looking for by viewing
them by category.
* I can view recipes I have uploaded.
* I can edit my own recipes.
* I can delete my own recipes.


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



## Features



**Features To Implement**

Ratings & Comments - It would be a helpful and nice feature if users could rate the recipes and comment on them.

Images - Ideally, image submission should happen through uploading the files themselves rather than entering a URL due potential issues with images hosted elsewhere.

More detailed userpages - The site is ‘communal’ in a way and it would be a beneficial feature if users could upload an image of themselves and perhaps an About section where they can write a bit about themselves and their particular interests related to cooking.

Following users - A feature to allow users to follow others and get notifications about recipes added.

A search functionality for keywords to help people find what they want once the collection size increased

** **

## Technologies used

* HTML5
* CSS3
* JavaScript
* Materialize
* Python
* Flask
* MongoDB
* JQuery
* Google Fonts
* Font Awesome

** **

## Frameworks, Libraries & programs

1. 
* 


** **

## Testing

W3C Markup Validator [Results]

W3C CSS Validator [Results]

**Known Issues**

* 

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
** **

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

## Testing User Requirements In UX section



## Credits

**Code**



**Content**



**Media**



**Acknowledgments**