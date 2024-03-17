import sys 
import pandas as pd 

from visa_approval.cloud.aws_storage import SimpleStorageService
from visa_approval.exception import USVisaException
from visa_approval.logger import logging 
from visa_approval.entity.estimator import USVisaModel




class USVisaEstimator:


    def __init__(self,bucket_name,model_path,):
        self.bucket_name = bucket_name
        self.s3 = SimpleStorageService()
        self.model_path = model_path
        self.loaded_model:USVisaModel=None

    def is_model_present(self,model_path):
        try:
            return self.s3.s3_key_path_available(bucket_name=self.bucket_name, s3_key=model_path)
        except USVisaException as e:
            print(e)
            return False
        

    def load_model(self,) -> USVisaModel:
        return self.s3.load_model(self.model_path,bucket_name=self.bucket_name)
    


    def save_model(self,from_file,remove:bool=False)->None:
        try:
            self.s3.upload_file(from_file,
                                to_filename=self.model_path,
                                bucket_name=self.bucket_name,
                                remove=remove
                                )
        except Exception as e:
            raise USVisaException(e, sys)
        


    def predict(self,dataframe:pd.DataFrame):

        try:
            if self.loaded_model is None:
                self.loaded_model = self.load_model()
            return self.loaded_model.predict(dataframe=dataframe)
        except Exception as e:
            raise USVisaException(e, sys)