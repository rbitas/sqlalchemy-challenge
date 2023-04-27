# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return ("""Welcome to Climate Analysis API! <br/> 
            Here are available routes: <br/>
            /api/v1.0/precipitation <br/>
            /api/v1.0/stations <br/>
            /api/v1.0/tobs <br/>
            /api/v1.0/<start> <br/>
            /api/v1.0/<start>/<end> 
            """)

@app.route('/api/v1.0/precipitation')
def precipitation():
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()
    session.close()

    all_precip = []
    for date, prcp in precipitation_data:
        precip_dict ={}
        precip_dict[date]= prcp
        all_precip.append(precip_dict)
    return jsonify(all_precip)

if __name__ == '__main__':
    app.run(debug=True)