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
#print(Base.classes.keys())
# Save reference to table
listings = Base.classes.AB_NYC_2019

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

#Add other routes here:
@app.route("/Brooklyn")
def Brooklynplot():
    graphplot(BrooklynDF)
    return render_template("brooklyn.html")

@app.route("/Queens")
def Queensplot():
    graphplot(QueensDF)
    return render_template("queens.html")

@app.route("/Manhattan")
def Manplot():
    graphplot(ManhattanDF)
    return render_template("manhattan.html")

@app.route("/Bronx")
def Bronxplot():
    graphplot(bronxDF)
    return render_template("bronx.html")

if __name__ == "__main__":
    app.run()
