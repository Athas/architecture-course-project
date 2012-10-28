from flask import request
from wsgi import app
from datastore import TruckData, database
import datetime, json

@app.route('/data', methods=['POST'])
def recent_data():
    database.connect()
    collected = []
    for truck, points in json.loads(request.data):
        for time, coords in points:
            new = TruckData()
            new.timestamp = float(time)
            new.truck_id = int(truck)
            new.latitude = float(coords[0])
            new.longitude = float(coords[1])
            new.save()
            collected.append(new)
    return json.dumps([c.get_default_dict() for c in collected])
    database.close()
