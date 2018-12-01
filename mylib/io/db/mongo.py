"""
Classes and methods necessary to input and output data from a MongoDB database. 

"""
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from bson.json_util import dumps
from bson.BSON import encode

class mongo_manager():
    '''
    Class to handle database access and loading/unloading of data
    
    Attributes
    ----------
    is_connected: boolean
        True/False if is there a database connection
    db: MongoClient
        MongoDB client connection to the active database
    db_name: String
    
    
    Methods
    -------
    connect('newdb')
        Connects to a database named newdb or creates one if it doesn't exist
    
    '''
    def __init__(self):
        self.is_connected = False
        self.db = None
        self.db_name = None
        
        
    def connect(self,db_name, host='localhost',
                           port=27017, username=None, password=None):
        """ 
        Get named database from MongoDB with/out authentication
        
        Parameters
        ----------
        db_name: string
                Name of MongoDB database
        host: string
                IP address or URI of host server
        port: integer
                Default port is 27017
        username: string
        password: string
        
        Returns
        -------
        MongoClient
            MongoClient connected to the specified database
        
        
        
         """
        # make Mongo connection with or without authentication
        if username and password:
            mongo_uri = 'mongodb://{username}:{password}@{host}/{db_name}'.format(username=username, password=password, host=host, db_name=db_name)
            conn = MongoClient(mongo_uri)
        else:
            conn = MongoClient(host, port)
    
            #set db settings?
            
            # Check for active connection
            try:
                if conn.server_info():
                    self.is_connected=True
            except ServerSelectionTimeoutError as e:
                print(e)  
                          
        self.db = conn[db_name]
    
    

    def export(self,what='db',extension="bson"):
        """    
        Export the database in a given format bson, or json
        
        #TODO add zip/tar functionality
        
        Parameters
        ----------
        what: string
            What should exported. 'db'  for the entire database or 'colllection name' for a single collection.
        extension: string
            Data type for export. Valid types include "json" and "bson"
            
        Returns
        -------
        boolean
            True if data exported properly. False if a fault occurred.
        
        """    
        if self.is_connected:
            
            if extension in ["bson","json",'csv','excel'] :
                json={}
                if what == 'db':
                    colls = self.db.list_database_names()
                else:
                    colls = what
                for coll in colls:
                    json[coll] = dumps(self.db.get_collection(coll).find()) # dumps creates a json string from the query
                    
                if extension is "bson":
                    return encode(json)
                elif extension in ["csv","excel"]:
                    import flatten_json #may not work as desired
                    flat_json = flatten_json.flatten(json)   
                    #create buffered string
                    #title=generate header
                    #cw = csv.DictWriter(f,title,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
                    #cw.writeheader()
                    #cw.writerows(flat_json)
                #for coll in self.
