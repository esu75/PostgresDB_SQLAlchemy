import sqlalchemy
from flask import Flask, jsonify
import datetime as dt
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# Database Setup
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Routes
@app.route("/")
def main():
    return (
        f"Welcome to the Climate App_API Home Page!<br>"
        f"Available Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/start<br>"
        f"/api/v1.0/start/end"
    )
    
@app.route("/api/v1.0/precipitation")
def precip():
    #most_recent_date  = session.query(Measurement.date).\
        #order_by(Measurement.date.desc()).first()
    one_year_from_most_recent_date = dt.date(2017,8,23)- dt.timedelta(days=365)
    Date_and_prcp = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_from_most_recent_date).\
                order_by(Measurement.date).all()
    session.close()

    
    
    list_prcp = []
    for date,prcp in Date_and_prcp:
        dict_prcp = {}
        dict_prcp[date] = prcp
        list_prcp.append(dict_prcp)

    return jsonify(list_prcp)

@app.route("/api/v1.0/stations")
def stations():
    most_active_stations = session.query(Measurement.station,func.count(Measurement.id)).\
        group_by(Measurement.station).order_by(func.count(Measurement.id).desc()).all()

    
    session.close()
    list_station = []
    for station, id in most_active_stations:
        dict_station = {}
        dict_station[station] = id
        list_station.append(dict_station)
    return jsonify(list_station)
# Query the dates and temperature observations of the most-active station for the previous
# year of data.Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    max_temp_obs = session.query(Measurement.station, Measurement.tobs).\
        filter(Measurement.date >= '2016-08-23').\
        filter(Measurement.station == 'USC00519281').all()

    
    session.close()
    #The following will return the previous year (date) and temperature for the
    # most active station, USC00519281 
    list_tobs = []
    for date, tobs in max_temp_obs:
        dict_tobs = {}
        dict_tobs[date] = tobs
        list_tobs.append(dict_tobs)
    return jsonify(list_tobs)

# Return a JSON list of the minimum temperature, the average temperature, and the maximum
# temperature for a specified start or start-end range.
@app.route("/api/v1.0/start")
def start():
    #start date = 2016-08-23
    stat_tobs = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
                   func.max(Measurement.tobs)).filter(Measurement.date == '2016-08-23').all()
    
    session.close()

    list_stat_tobs = [] #list to hold the dictionary values as a dict in a list [{}]

    for min,avg,max in stat_tobs:
        # Dictionary to hold the key and the value.
        dict_stat_tobs = {}
        dict_stat_tobs["TMIN"] = min
        dict_stat_tobs["TAVG"] = avg
        dict_stat_tobs["TMAX"] = max
        
        list_stat_tobs.append(dict_stat_tobs)
        
    return jsonify(list_stat_tobs)

@app.route('/api/v1.0/<start>/<end>')
def start_end(start,end):
    Start_end_summary = session.query(func.min(Measurement.tobs), \
                                      func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
                                        filter(Measurement.date >= '2016-08-23').\
                                            filter(Measurement.date <= '2017-08-23').all()

    session.close()

    list_Start_end = []
    for min, avg, max in Start_end_summary:
        dict_Start_end = {}
        dict_Start_end["TAVG"] = avg
        dict_Start_end["TMIN"] = min
        dict_Start_end["TMAX"] = max
       
        
        list_Start_end.append(dict_Start_end)

    return jsonify(list_Start_end)


if __name__ == '__main__':
    app.run(debug=True)