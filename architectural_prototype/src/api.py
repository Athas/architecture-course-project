from flask import Flask
app = Flask(__name__)

@app.route('/data')
def recent_data():
    return 'Fetch recent data.'

@app.route('/data/<truck_id>')
def truck_data(truck_id):
    return 'Fetch recent data for truck: ' + str(truck_id) + '.'

@app.route('/data/<float:lat>/<float:lon>/<float:radius>')
def location_data(lat, lon, radius):
    return "Fetch trucks within " + radius + "km of " + str(lat) + ":" + str(lon)

if __name__ == '__main__':
    app.run()
