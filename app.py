# Dependencies
# ----------------------------------
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################
#CONFIGURE DATABASE:
# ----------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/FINALdb.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)
# Save references to each table
# Print all of the classes mapped to the Base
print(Base.classes.keys())
# Save reference to table
listings = Base.classes.AB_NYC_2019
def Select_B(neighbourhood_group):
    """Return the Brooklyn Data"""
    sel = [
        listings.id,
        listings.name,
        listings.neighbourhood_group,
        listings.latitude,
        listings.longitude,
        listings.room_type,
        listings.price,
        listings.minimum_nights
    ]

    results = db.session.query(*sel).filter(listings.neighbourhood_group == neighbourhood_group).all()

    #return results
    #Create a dictionary entry for each row of listings information
    listings_list = []
    for result in results:
        listing = {}
        listing["id"] = result[0]
        listing["name"] = result[1]
        listing["neighbourhood_group"] = result[2]
        listing["latitude"] = result[3]
        listing["longitude"] = result[4]
        listing["room_type"] = result[5]
        listing["price"] = result[6]
        listing["minimum_nights"] = result[7]
        listings_list.append(listing)
    
    return listings_list

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/Brooklyn")
def Brooklynplot():    
    print("Brooklyn route works!")
    return jsonify(Select_B("Brooklyn"))
    # return render_template("Brooklyn.html")


@app.route("/Queens")
def Queensplot():
    Select_B(Queens)
    return render_template("queens.html")

@app.route("/Manhattan")
def Manplot():
    Select_B(Manhattan)
    return render_template("manhattan.html")

@app.route("/Bronx")
def Bronxplot():
    Select_B(Bronx)
    return jsonify(Select_B)
    return render_template("bronx.html")

if __name__ == "__main__":
    app.run()

#Will use this function in app.js to create charts for each borough
