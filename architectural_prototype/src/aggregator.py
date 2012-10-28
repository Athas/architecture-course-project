from flask import request
from wsgi import app
from datastore import TruckData
import datetime, json

@app.route('/data', methods=['POST'])
def recent_data():
    data = json.loads(request.data)
    collected = []
    for d in data:
        new = TruckData()
        new.timestamp = 
        new.truck_id = request.form['truck_id']
        new.latitude = float(request.form['latitude'])
        new.longitude = float(request.form['longitude'])
        new.save()
        collected.append(new)
    return json.dumps([c.get_default_dict() for c in collected])


