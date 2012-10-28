from db import SimpleDb
    
class Datastore(SimpleDB):
    def __init__(self, domain="datastore"):
        super(domain)
        
    def new_entry(self, truck_id, timestamp, lat, lon):
        entry = self.domain.new_item(str(truck_id) + str(timestamp))
        entry['truck_id'] = truck_id
        entry['timestamp'] = timestamp
        entry['lat'] = lat
        entry['lon'] = lon
        entry.save()
        return entry
    
    def new_entries(self, points):
        for p in points:
            self.new_entry(
                p['truck_id'],
                p['timestamp'],
                p['lat'],
                p['lon']
                )
