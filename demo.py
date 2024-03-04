from visa_approval.configuration.mongodb_connector import MongoDBClient 

connector = MongoDBClient()
c, d ,dnm  = connector.connection_status()
print(c)
print(100*'-')
print(d)
print(100*'-')
print(dnm)