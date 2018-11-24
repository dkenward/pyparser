"""
Classes and methods necessary to input and output data from a MongoDB database. 

"""
from pymongo import MongoClient


class mydb():
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
        # make Mongo connection with/out authentication
        if username and password:
            mongo_uri = 'mongodb://%s:%s@%s/%s'
            (username, password, host, db_name)
            conn = MongoClient(mongo_uri)
        else:
            conn = MongoClient(host, port)
    
        return conn[db_name]
    
    

    def export(self,extension="bson"):
        """    
        Export the database in a given format bson, or json
        
        #TODO add zip/tar functionality
        
        Parameters
        ----------
        extension: string
            Data type for export. Valid types include "json" and "bson"
            
        Returns
        -------
        boolean
            True if data exported properly. False if a fault occurred.
        
        """    
        if self.is_connected:
            #TODO: complete function
            if extension is "bson":
                pass
            elif extension is "json":
                pass
            pass
