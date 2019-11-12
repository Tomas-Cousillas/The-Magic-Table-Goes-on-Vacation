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

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/Brooklyn")
Select_B(Bronx)
    return jsonify(Select_B)
    return render_template("Brooklyn.html")


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

    return results