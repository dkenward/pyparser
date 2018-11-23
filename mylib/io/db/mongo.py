from pymongo import MongoClient


'''
Database class to handle transactions, ensure json is formed appropriately, etc.

'''
class mydb():
    
    '''
    Connect to the database
    '''
    def connect(db_name, host='localhost',\
                           port=27017, username=None, password=None):
        """ Get named database from MongoDB with/out authentication """
        # make Mongo connection with/out authentication
        if username and password:
            mongo_uri = 'mongodb://%s:%s@%s/%s'
            (username, password, host, db_name)
            conn = MongoClient(mongo_uri)
        else:
            conn = MongoClient(host, port)
    
        return conn[db_name]
    
    
    '''
    Export the database in a given format, bson, json, zipped, tarred as needed.
    
    '''
    def export(self,extension="bson",):
    
    