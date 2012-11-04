import peewee


# Local SQLite Database for testing

database = peewee.SqliteDatabase('temp.db')
        
class TruckData(peewee.Model):
    class Meta:
        database = database
    
    truck_id = peewee.IntegerField()
    timestamp = peewee.FloatField()
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()
    
    def get_default_dict(self):
        return {
            'truck_id': self.truck_id,
            'timestamp': self.timestamp,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

database.connect()
try:
    TruckData.create_table()
except:
    print "TruckData table already exists!"
database.close()

#Amazon SimpleDB Database for Evaluation
import boto

AWS_KEY = ""
AWS_SECRET_KEY = ""

class SimpleDB:
    def __init__(self, domain):
        self.sdb = boto.connect_sdb(AWS_KEY, AWS_SECRET_KEY)
        self.domain = self.sdb.create_domain(domain)
    
class Datastore(SimpleDB):
    def __init__(self, domain="datastore"):
        super(domain)
    
    def new_entry(self, truck_id, timestamp, lat, lon):
        entry = self.domain.new_item()
        entry['truck_id'] = truck_id
        entry['timestamp'] = timestamp
        entry['lat'] = lat
        entry['lon'] = lon
        entry.save()
        return entry
    
    def new_entries(self, points):
        values = {}
        for p in points:
            key = str(p['truck_id']) + str(p['timestamp'])
            values[key] = p
        self.domain.batch_put_attributes(values)
    
    def get_all_data(self):
        return [p for p in self.domain]
    
    def query_by_truck(self, truck_id, min_time=None, max_time=None):
        query_string = "'%s'='%s'" % ("truck_id", truck_id)
        if min_time:
            query_string += " and '%s'>'%s'" % ("timestamp", str(min_time))
        if max_time:
            query_string += " and '%s'<'%s'" % ("timestamp", str(max_time))
        
        return self.domain.query("[%s]" % query_string)
    
    def query_by_location(self, lat, lon, radius, min_time=None, max_time=None):
        query_string = "'%s'>'%s'" % ("lat", str(lat - radius))
        query_string += "'%s'<'%s'" % ("lat", str(lat + radius))
        query_string += "'%s'>'%s'" % ("lon", str(lon - radius))
        query_string += "'%s'<'%s'" % ("lon", str(lon + radius))
        if min_time:
            query_string += " and '%s'>'%s'" % ("timestamp", str(min_time))
        if max_time:
            query_string += " and '%s'<'%s'" % ("timestamp", str(max_time))
        
        return self.domain.query("[%s]" % query_string)

