from flask import request
from wsgi import app
from datastore import TruckData, database
import datetime, json

@app.route('/data', methods=['POST'])
def recent_data():
    database.connect()
    collected = []
    for truck, points in json.loads(request.data).iteritems():
        for time, coords in points.iteritems():
            new = TruckData()
            new.timestamp = float(time)
            new.truck_id = int(truck)
            new.latitude = float(coords[0])
            new.longitude = float(coords[1])
            new.save()
            collected.append(new)

    database.close()
    return "success"
