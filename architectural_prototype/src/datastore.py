import peewee

database = peewee.SqliteDatabase('temp.db')
        
class TruckData(peewee.Model):
    class Meta:
        database = database
    
    truck_id = peewee.IntegerField()
    timestamp = peewee.DateTimeField()
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()

database.connect()
TruckData.create_table()
