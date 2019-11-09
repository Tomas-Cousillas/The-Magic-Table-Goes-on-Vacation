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
# Create Database Connection
# ----------------------------------
engine = create_engine(f"sqlite:///db/FINALdb.sqlite")
conn = engine.connect()
# Query All Records in the the Database
dataframe = pd.read_sql("SELECT * FROM AB_NYC_2019", conn)
#transform the datafframe into a json object
#filter json objects into boroughs


#BrooklynDF = dataframe.loc[data["neighbourhood_group"] == "Brooklyn"]
#QueensDF = dataframe.loc[data["neighbourhood_group"] == "Queens"]
#ManhattanDF = dataframe.loc[data["neighbourhood_group"] == "Manhattan"]
#StatenDF = dataframe.loc[data["neighbourhood_group"] == "Staten Island"]
#BronxDF = dataframe.loc[data["neighbourhood_group"] == "Bronx"]


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
