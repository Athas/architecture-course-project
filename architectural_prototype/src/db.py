import boto

class SimpleDB:
    def __init__(self, aws_key, aws_secret_key, domain):
        self.sdb = boto.connect_sdb(aws_key, aws_secret_key)
        self.domain = self.sdb.create_domain(domain)
