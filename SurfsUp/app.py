# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
from datetime import timedelta

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
            <br/>
            Here are available routes: <br/>
            <br/>
            /api/v1.0/precipitation <br/>
            /api/v1.0/stations <br/>
            /api/v1.0/tobs <br/>
            <br/>
            Insert date starting with four digets for year, two for month and day: <br/>
            /api/v1.0/yyyy-mm-dd <br/>
            /api/v1.0/yyyy-mm-dd/yyyy-mm-dd 
            """)

@app.route('/api/v1.0/precipitation')
def precipitation():
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()

    all_precip = []
    for date, prcp in precipitation_data:
        precip_dict ={}
        precip_dict[date]= prcp
        all_precip.append(precip_dict)
    return jsonify(all_precip)

@app.route('/api/v1.0/stations')
def station():
    results = session.query(Station.station).order_by(Station.station).all()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route('/api/v1.0/tobs')
def tobs():
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temperature_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= year_ago).filter(Measurement.station == 'USC00519281').all()

    session.close()

    year_temp = []
    for date, tobs in temperature_data:
        temp_dict = {}
        temp_dict['date'] = date
        temp_dict['tobs'] = tobs
        year_temp.append(temp_dict)
    return jsonify(year_temp)


@app.route('/api/v1.0/<start>')
def start_temp(start = '2010-01-01'):
    session = Session(engine)
    query_results = session.query(func.avg(Measurement.tobs), func.min(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start)
    
    session.close()
    
    start_date = []
    for avg, min, max in query_results:
        start_date_dict = {}
        start_date_dict['Average Temp'] = avg
        start_date_dict['Minimum Temp'] = min
        start_date_dict['Maximum Temp'] = max
        start_date.append(start_date_dict)
    return jsonify(start_date)

@app.route('/api/v1.0/<start>/<end>')
def end_temp(start= '2010-01-01', end= '2017-08-23'):
    end_temp = session.query(func.avg(Measurement.tobs), func.min(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).group_by(Measurement.date).all()
    
    end_date = []
    for avg, min, max in end_temp:
        end_date_dict = {}
        end_date_dict['Average Temp'] = avg
        end_date_dict['Minimum Temp'] = min
        end_date_dict['Maximum Temp'] = max
        end_date.append(end_date_dict)
    return jsonify(end_date)


if __name__ == '__main__':
    app.run(debug=True)