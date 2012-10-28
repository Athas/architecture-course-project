import peewee

database = peewee.SqliteDatabase('sqlite:///:memory:')
        
class TruckData:
    class Meta:
        database = database
    
    truck_id = peewee.IntegerField()
    timestamp = peewee.DateTimeField()
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()

database.connect()
TruckData.create_table()
