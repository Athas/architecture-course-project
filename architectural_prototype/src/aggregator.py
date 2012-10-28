from flask import request
from wsgi import app
from datastore import TruckData, database
import datetime, json

@app.route('/data', methods=['POST'])
def recent_data():
    database.connect()
    data = json.loads(request.data)
    collected = []
    for truck, items in data:
        for time, coords in items:
            new = TruckData()
            new.timestamp = float(time)
            new.truck_id = int(truck)
            new.latitude = float(coords[0])
            new.longitude = float(coords[1])
            new.save()
            collected.append(new)
            print json.dumps(new.get_default_dict())
    return json.dumps([c.get_default_dict() for c in collected])
    database.close()


