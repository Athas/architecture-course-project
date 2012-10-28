from wsgi import app
from datastore import TruckData

@app.route('/data')
def recent_data():
    query = TruckData.select().order_by(TruckData.timestamp.desc())
    data = [d.get_default_dict() for d in query]
    return json.dumps(data)

@app.route('/data/<truck_id>')
def truck_data(truck_id):
    query = TruckData.select()
    query = query.where(TruckData.truck_id == truck_id)
    query = query.order_by(TruckData.timestamp.desc())
    data = [d.get_default_dict() for d in query]
    return json.dumps(data)

@app.route('/data/<float:lat>/<float:lon>/<float:radius>')
def location_data(lat, lon, radius):
    # NOTE: the "radius" is a square threshold, not circular
    query = TruckData.select()
    query = query.where(TruckData.latitude > lat - radius)
    query = query.where(TruckData.latitude < lat + radius)
    query = query.where(TruckData.longitude > lon - radius)
    query = query.where(TruckData.longitude < lon + radius)
    query = query.order_by(TruckData.timestamp.desc())
    data = [d.get_default_dict() for d in query]
    return json.dumps(data)
