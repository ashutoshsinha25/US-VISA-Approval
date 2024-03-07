import sys 

from visa_approval.components.data_ingestion import DataIngestion 
from visa_approval.entity.config_entity import DataIngestionConfig 
from visa_approval.entity.artifact_entity import DataIngestionArtifact 

from visa_approval.exception import USVisaException
from visa_approval.logger import logging 


class TrainPipeline:

    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:

        try:
            logging.info("Entered start_data-ingestion method of class TrainPiple class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion() 
            logging.info("train and test data received from db")
            logging.info("Exiting start_data_ingestion method of class TrainPipeline")
            return data_ingestion_artifact 
        except Exception as e:
            raise USVisaException(e, sys) from e

    def ru_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise USVisaException(e, sys) from e
