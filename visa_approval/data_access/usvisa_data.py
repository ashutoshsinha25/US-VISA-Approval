from visa_approval.configuration.mongodb_connector import MongoDBClient 
from visa_approval.constant import DATABASE_NAME 
from visa_approval.exception import USVisaException 

import pandas as pd 
import numpy as np 

import sys 
from typing import Optional 

class USVisaData:
    """
    This class helps to export entire db records as a pandas df
    """

    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_nm=DATABASE_NAME)
        except Exception as e:
            raise USVisaException(e,sys) from e 
        
    
    def export_collection_as_df(self,collection_nm:str, database_nm:Optional[str]=None) -> pd.DataFrame:
        try:
            if database_nm is None:
                _, db ,_ = self.mongo_client.connection_status()
                collection = db[collection_nm]
            else:
                collection = self.mongo_client[database_nm][collection_nm]

            df = pd.DataFrame(list(collection.find()))
            if '_id' in df.columns.to_list():
                df = df.drop(columns=['_id'],axis=1)
            
            df.replace({'na' : np.nan} , inplace=True)
            return df
        except Exception as e:
            raise USVisaException(e , sys) from e