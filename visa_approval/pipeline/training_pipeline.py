import sys 

from visa_approval.components.data_ingestion import DataIngestion 
from visa_approval.entity.config_entity import DataIngestionConfig 
from visa_approval.entity.artifact_entity import DataIngestionArtifact 

from visa_approval.components.data_validation import DataValidation
from visa_approval.entity.config_entity import DataValidationConfig 
from visa_approval.entity.artifact_entity import DataValidationArtifact

from visa_approval.exception import USVisaException
from visa_approval.logger import logging 


class TrainPipeline:

    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()



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



    def start_data_validation(self, data_ingestion_artifact : DataIngestionArtifact) -> DataIngestionArtifact:
        logging.info("Entering the satrt_data_validation method of TrainPipeline class")
        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact ,
                                             data_validation_config= self.data_validation_config)
            
            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed data validation ")
            logging.info("Exited start_data_validation method of class TrainPipeline Class")
            return data_ingestion_artifact
        except Exception as e:
            raise USVisaException(e, sys) from e


    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)

        except Exception as e:
            raise USVisaException(e, sys) from e
