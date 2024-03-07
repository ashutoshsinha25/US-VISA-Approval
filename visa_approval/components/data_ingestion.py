import os 
import sys 

from pandas import DataFrame 
from sklearn.model_selection import train_test_split 

from visa_approval.entity.config_entity import DataIngestionConfig 
from visa_approval.entity.artifact_entity import DataIngestionArtifact 
from visa_approval.exception import USVisaException 
from visa_approval.logger import logging 
from visa_approval.data_access.usvisa_data import USVisaData 



class DataIngestion:

    def __init__(self,data_ingestion_config : DataIngestionConfig = DataIngestionConfig() ):

        try:
            self.data_ingestion_config = data_ingestion_config 
        except Exception as e:
            raise USVisaException(e,sys) from e 
        

    def export_data_into_feature_store(self):
        

        try:

            logging.info("Exporting data from mongodb")
            usvisa_data = USVisaData() 
            df = usvisa_data.export_collection_as_df(
                collection_nm= self.data_ingestion_config.collection_nm
            )
            logging.info(f"Shape of the dataframe {df.shape}")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path 
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path : {feature_store_file_path}")
            df.to_csv(feature_store_file_path, index=False , header=True)
            return df 
        except Exception as e:
            raise USVisaData(e, sys) from e 
    

    def split_data_as_train_test(self,df : DataFrame) -> None:
        
        logging.info("Entered split_data_as_train_test method of DataIngestion class")

        try:
            train, test = train_test_split(df, test_size = self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the df")
            logging.info("Exited split_data_as_train_test method of DataIngestion class")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path , exist_ok=True)

            logging.info(f"Exporting train and test to file path ")
            train.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info(f"Exported the data to : {self.data_ingestion_config.training_file_path} and {self.data_ingestion_config.testing_file_path}")

        except Exception as e:
            raise USVisaException(e, sys) from e
        
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:

        logging.info("Entering initiate_data_ingestion method of DataIngestion class")
        try:
            df = self.export_data_into_feature_store() 
            logging.info("Data stored from mongodb")
            self.split_data_as_train_test(df)
            logging.info("train test split done on the dataframe")
            logging.info("Exited initiate_data_ingestion method")

            data_ingestion_artifact = DataIngestionArtifact(
                                    trained_file_path=self.data_ingestion_config.training_file_path,
                                    test_file_path=self.data_ingestion_config.testing_file_path)
            logging.info(f"Data Ingestion artifact : {data_ingestion_artifact}")
            return data_ingestion_artifact 
        except Exception as e:
            raise USVisaException(e,sys) from e
        





