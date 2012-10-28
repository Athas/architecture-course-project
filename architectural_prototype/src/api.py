from wsgi import app
from datastore import TruckData, database
import json

@app.route('/api/all')
def all_data():
    database.connect()
    query = TruckData.select().order_by(TruckData.timestamp.desc())
    data = [d.get_default_dict() for d in query]
    return json.dumps(data)
    database.close()

@app.route('/api/truck/<int:truck_id>')
def truck_data(truck_id):
    database.connect()
    query = TruckData.select()
    query = query.where(TruckData.truck_id == truck_id)
    query = query.order_by(TruckData.timestamp.desc())
    data = [d.get_default_dict() for d in query]
    return json.dumps(data)
    database.close()

@app.route('/api/location/<float:lat>/<float:lon>/<float:radius>')
def location_data(lat, lon, radius):
    database.connect()
    # NOTE: the "radius" is a square threshold, not circular
    query = TruckData.select()
    query = query.where(TruckData.latitude > lat - radius)
    query = query.where(TruckData.latitude < lat + radius)
    query = query.where(TruckData.longitude > lon - radius)
    query = query.where(TruckData.longitude < lon + radius)
    query = query.order_by(TruckData.timestamp.desc())
    data = [d.get_default_dict() for d in query]
    return json.dumps(data)
    database.close()
