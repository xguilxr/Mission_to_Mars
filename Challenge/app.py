# Dependencies
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
# from flask_table import Table, Col

import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_app'
mongo = PyMongo(app)

# Index route
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html",mars=mars)

#  Scrape route
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run()