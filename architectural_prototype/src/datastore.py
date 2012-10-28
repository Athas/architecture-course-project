from db import SimpleDb
    
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
