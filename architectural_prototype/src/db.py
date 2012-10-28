import boto
from config import AWS_KEY, AWS_SECRET_KEY

class SimpleDB:
    def __init__(self, domain):
        self.sdb = boto.connect_sdb(AWS_KEY, AWS_SECRET_KEY)
        self.domain = self.sdb.create_domain(domain)
