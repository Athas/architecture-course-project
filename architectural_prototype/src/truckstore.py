from db import SimpleDB

class Truckstore(SimpleDB):
    def __init__(self, domain="truckstore"):
        super(domain)
    
    def new_entry(self, truck_id):
        entry = self.domain.new_item(str(truck_id))
        entry['active'] = "True"
        entry.save()

    def new_entries(self, truck_ids):
        for i in truck_ids:
            self.new_entry(i)
    
    def deactivate_truck(self, truck_id):
        entry = self.domain.get_item(str(truck_id))
        entry['active'] = "False"
        entry.save()

    def reactivate_truck(self, truck_id):
        entry = self.domain.get_item(str(truck_id))
        entry['active'] = "True"
        entry.save()

    def verify_truck_id(self, truck_id):
        entry = self.domain.get_item(str(truck_id))
        return entry and 'active' in entry and entry['active'] == "True"
    
    def get_active_trucks(self):
        return [i.name for i in self.domain if i['active'] == "True"]
        
