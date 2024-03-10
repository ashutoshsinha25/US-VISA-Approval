import json 
import sys 

import pandas as pd 
from pandas import DataFrame
from evidently.model_profile import Profile 
from evidently.model_profile.sections import DataDriftProfileSection 


from visa_approval.exception import USVisaException 
from visa_approval.logger import logging 
from visa_approval.utils.main_utils import read_yaml_file, write_yaml_file
from visa_approval.entity.config_entity import DataIngestionConfig , DataValidationConfig
from visa_approval.entity.artifact_entity import DataIngestionArtifact , DataValidationArtifact 
from visa_approval.constant import SCHEMA_FILE_PATH



class DataValidation:

    def __init__(self, data_ingestion_artifact: DataIngestionArtifact ,
                 data_validation_config: DataValidationConfig ) -> None:
        
        
        try:
            self.data_ingestion_artifact = data_ingestion_artifact 
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise USVisaException(e, sys) from e 
        

    def validate_number_of_columns(self, df:DataFrame) -> bool:


        try:
            status = len(df.columns) == len(self._schema_config['columns'])
            logging.info(f"All Columns present : {status}")
            return status 
        except Exception as e:
            raise USVisaException(e, sys) from e
        

    def is_column_exists(self, df : DataFrame) -> bool:


        try:
            df_cols = df.columns 
            missing_num_cols = [] 
            missing_cat_cols = [] 

            for col in self._schema_config['numerical_columns']:
                if col not in df_cols:
                    missing_num_cols.append(col)
            for col in self._schema_config['categorical_columns']:
                if col not in df_cols:
                    missing_cat_cols.append(col)

            if len(missing_num_cols) > 0:
                logging.info(f"Missing num cols : {missing_num_cols}")
            
            if len(missing_cat_cols) > 0:
                logging.info(f"Missing cat cols : {missing_cat_cols}")

            return False if len(missing_num_cols) > 0 or len(missing_cat_cols) else True 
        except Exception as e:
            raise USVisaException(e, sys) from e 
        


    @staticmethod
    def read_data(file_path) -> DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise USVisaException(e, sys)
        

    
    def detect_dataset_drift(self, ref_df: DataFrame , curr_df : DataFrame) -> bool :


        try:
            data_drift_profile = Profile(sections=[DataDriftProfileSection()])
            data_drift_profile.calculate(ref_df,  curr_df )

            report = data_drift_profile.json() 
            json_report = json.loads(report)
            
            write_yaml_file(file_path = self.data_validation_config.drift_report_file_path , content= json_report)
            
            n_features = json_report['data_drift']['data']["metrics"]['n_features']
            n_drifted_features = json_report['data_drift']['data']["metrics"]['n_drifted_features']

            logging.info(f"{n_drifted_features}/{n_features} drifts were detected")
            drift_status = json_report['data_drift']['data']['metrics']['dataset_drift']
            return drift_status 
        except Exception as e:
            raise USVisaException(e, sys) from e 
        

    
    def initiate_data_validation(self) -> DataValidationArtifact:


        try:
            validation_error_msg = "" 
            logging.info("Starting data validation ")

            train, test = (DataValidation.read_data(file_path=self.data_ingestion_artifact.trained_file_path),
                           DataValidation.read_data(file_path=self.data_ingestion_artifact.test_file_path))
            
            status = self.validate_number_of_columns(df=train )
            logging.info(f"required cols present in training df : {status}")
            if not status :
                validation_error_msg += f"Cols are missing in training data"
        
            status = self.validate_number_of_columns(df = test)
            logging.info(f"required cols present in testing df : {status}")
            if not status :
                validation_error_msg += f"Cols are missing in testing data"

            status = self.is_column_exists(df=train)
            if not status :
                validation_error_msg += f"Cols are missing in traning data"
            
            status = self.is_column_exists(df=test)
            if not status:
                validation_error_msg += f"Cols are missing in testing data"

            
            validataion_status = len(validation_error_msg) == 0
            if validataion_status:
                drift_status = self.detect_dataset_drift(train, test)
                if drift_status:
                    logging.info("Drift detected")
                    validation_error_msg = 'Drift detected'
                else:
                    validation_error_msg = 'Drift not detected'
            else:
                logging.info(f"Validation error : {validation_error_msg}")


            

            data_validation_artifact = DataValidationArtifact(
                validation_status=validataion_status,
                message=validation_error_msg,
                drift_report_file_path=self.data_validation_config.drift_report_file_path
            )


            logging.info(f"Data validation artifact : {data_validation_artifact}")
            return data_validation_artifact 
        except Exception as e:
            raise  USVisaException(e, sys) from e 
