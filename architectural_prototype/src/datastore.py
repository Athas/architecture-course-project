import peewee

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
