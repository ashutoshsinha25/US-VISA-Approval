import os 
import sys 

import numpy as np 
import pandas as pd 
from pandas import DataFrame 

from visa_approval.entity.config_entity import USVisaPredictorConfig 
from visa_approval.entity.s3_estimator import USVisaEstimator 
from visa_approval.exception import USVisaException 
from visa_approval.logger import logging 


class USVisaData:

    def __init__(self, 
                 continent,
                 education_of_employee,
                 has_job_experience,
                 requires_job_training,
                 no_of_employees,
                 region_of_employment,
                 prevailing_wage,
                 unit_of_wage,
                 full_time_position,
                 company_age):
        
        try:
            self.continent = continent
            self.eduction_of_employee = education_of_employee 
            self.has_job_experience = has_job_experience 
            self.requires_job_training = requires_job_training
            self.no_of_employees = no_of_employees 
            self.region_of_employment = region_of_employment 
            self.prevailing_wage = prevailing_wage 
            self.unit_of_wage = unit_of_wage 
            self.full_time_position = full_time_position  
            self.company_age = company_age 

        except Exception as e:
            raise USVisaException(e, sys) from e 
        
    
    def get_visa_data_dict(self):

        logging.info('entered get_visa_data_dict ,ethod for USVisaData class')
        try:
            input_data = {
                'continent' : [self.continent],
                'education_of_employee' : [self.eduction_of_employee],
                'has_job_experience' : [self.has_job_experience],
                'requires_job_training' : [self.requires_job_training],
                'no_of_employees' : [self.no_of_employees],
                'region_of_employment' : [self.region_of_employment],
                'prevailing_wage' : [self.prevailing_wage],
                'unit_of_wage' :[self.unit_of_wage],
                'full_time_position' : [self.full_time_position],
                'company_age' : [self.company_age]
            }
            logging.info("Created usvisa data dict")
            logging.info("Exited get_visa_data_dict method as USVisaData class")
            return input_data 
        except Exception as e:
            raise USVisaException(e, sys) from e 


    def get_visa_input_df(self) -> DataFrame :


        try:
            visa_dict = self.get_visa_data_dict()
            return DataFrame(visa_dict)
        except Exception as e:
            raise USVisaException(e, sys) from e
        
    

class USVisaClassifier:

    def __init__(self, prediction_pipeline_config : USVisaPredictorConfig = USVisaPredictorConfig()) -> None:

        try:
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise USVisaException(e, sys) from e 

    def predict(self, df ) -> DataFrame :
        try:
            logging.info("entered predict method of USVisaClassifer class")
            model = USVisaEstimator(
                bucket_name = self.prediction_pipeline_config.model_bucket_name,
                model_path = self.prediction_pipeline_config.model_file_path
            )
            result = model.predict(df)
            return result   
        
        except Exception as e:
            raise USVisaException(e, sys) from e 