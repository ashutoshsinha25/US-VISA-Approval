# creating a connecting with mongodb using mongodb client 
import sys
import os 
from visa_approval.exception import USVisaException 
from visa_approval.logger import logging 
from visa_approval.constant import DATABASE_NAME , MONGODB_URL_KEY 
import pymongo 
import certifi 

ca = certifi.where() 

class MongoDBClient:
    """
    This method connects with mongodb
    output : connection to mongodb database
    on failure : raises an exception 
    """
    client = None 

    def __init__(self, database_nm = DATABASE_NAME) -> None:
        logging.info("trying connection to mongodb")

        try:
            if MongoDBClient.client is None:
                mongodb_url = MONGODB_URL_KEY
                if mongodb_url is None:
                    raise Exception("Env key : MONGODB_URL_KEY is not correct.")
                MongoDBClient.client = pymongo.MongoClient(mongodb_url , tlsCAFile=ca)
            
            self.client=MongoDBClient.client 
            self.database = self.client[database_nm]
            self.database_nm = database_nm
            logging.info("mongodb connection successful")
        except Exception as e:
            raise USVisaException(e,sys) from e
        

    def connection_status(self):
        return self.client , self.database , self.database_nm

