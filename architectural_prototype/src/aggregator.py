from flask import request
from wsgi import app
from datastore import TruckData
import datetime, json

@app.route('/data', methods=['POST'])
def recent_data():
    new = TruckData()
    new.timestamp = datetime.datetime.now()
    new.truck_id = request.form['truck_id']
    new.latitude = float(request.form['latitude'])
    new.longitude = float(request.form['longitude'])
    new.save()
    return json.dumps(new.get_default_dict())


