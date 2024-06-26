# constants for the project 

import os 
from datetime import date 
from dotenv import load_dotenv 
_ = load_dotenv() 


DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "VISA_DATA"
MONGODB_URL_KEY = os.environ.get('MONGO_CONNECTION_STR')
ACCESS_KEY = os.environ.get('KEY')
SECRET_KEY = os.environ.get('SECRET')
REGION_NAME = "us-east-1"

PIPELINE_NAME : str = 'USVISA'
ARTIFACT_DIR : str = "artifact"

MODEL_FILE_NAME = 'model.pkl'

TARGET_COLUMN ='case_status'
CURRENT_YEAR = date.today().year 
PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'

FILE_NAME : str = "usvisa.csv"
TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'
SCHEMA_FILE_PATH: str = os.path.join("config" , "schema.yaml")


"""
Data Ingestion constants  ( starts with DATA_INGESTION var name)
"""
DATA_INGESTION_COLLECTION_NAME:str = 'VISA_DATA'
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR:str = 'feature_store'
DATA_INGESTION_INGESTED_DIR: str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2





"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str="data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = 'drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = 'report.yaml'



"""
Data Transformation ralated constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"




"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")



"""
MODEL EVALUATION related constant start with MODEL_EVALUATION var name
"""
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "usvisa-modelv0"
MODEL_PUSHER_S3_KEY = "model-registry"
