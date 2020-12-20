import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()

# Reflect hawaii database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# reflect the measurement table
measurement_data = pd.read_sql("SELECT * FROM measurement", conn)
measurement_data

# reflect an existing database into a new model
station_data = pd.read_sql("SELECT * FROM station", conn)
station_data

# Reflect Database into ORM class
Measurements = Base.classes.measurement
Stations= Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def Home page():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>" 
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Convert the query results to a dictionary using `date` as the key and `prcp` as the value."""
    
    session.close()

    
    return jsonify(precipitation)
@app.route("/api/v1.0/stations")
def stations():
     # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of stations from the dataset."""
    
    session.close()

    
    """* Return the JSON representation of your dictionary."""
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def temperatures():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """* Query the dates and temperature observations of the most active station for the last year of data."""
  
    """* Return a JSON list of temperature observations (TOBS) for the previous year."""
    
    session.close()
    
@app.route("/api/v1.0/<start>")
def start_date():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
        * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date."""

    # Convert list of tuples into normal list
    
    """* Return the JSON representation of your dictionary."""
    
    return jsonify(start_date)
    
    session.close()
    
@app.route("/api/v1.0/<start>/<end>")
def date_range():

# Create our session (link) from Python to the DB
    session = Session(engine)
    
    """When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive."""
    
    
    """* Return the JSON representation of your dictionary."""
    
    return jsonify(date_range)

    session.close()
    
if __name__ == '__main__':
    app.run(debug=True)