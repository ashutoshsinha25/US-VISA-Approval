# constants for the project 

import os 
from datetime import date 



DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "VISA_DATA"
MONGODB_URL_KEY = os.environ.get('MONGO_CONNECTION_STR')

PIPLELINE_NAME : str = 'USVISA'
ARTIFACT_DIR : str = "artifact"

MODEL_FILE_NAME = 'model.pkl'

TARGET_COLUMN ='case_status'
CURRENT_YEAR = date.today().year 
PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'

FILE_NAME : str = "usvisa.csv"
TRAIN_FILE_NAME: str = 'train.csv'
TESTS_FILE_NAME: str = 'test.csv'



"""
Data Ingestion constants  ( starts with DATA_INGESTION var name)
"""
DATA_INGESTION_COLLECTION_NAME:str = 'VISA_DATA'
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR:str = 'feature_store'
DATA_INGESTION_INGESTED_DIR: str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2