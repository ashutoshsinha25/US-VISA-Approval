# common function to be used for the project 

import os 
import sys 

import numpy as np 
import dill 
import yaml 
from pandas import DataFrame 

from visa_approval.exception import USVisaException 
from visa_approval.logger import logging 


def read_yaml_file(file_path : str) -> dict:
    try:
        with open(file_path , 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise USVisaException(e,sys) from e 
    

def write_yaml_file(file_path : str , content : object , replace : bool = False) -> None:
    try:
        if replace:
            if os.path.exist(file_path):
                os.remove(file_path)
        os.makedirs(os.path.join(file_path) , exist_ok=True)
        with open(file_path,'w') as f:
            yaml.dump(content , f)
    except Exception as e:
        raise USVisaException(e, sys)
    

def load_object(file_path : str) -> None:
    logging.info("Entered the load_object method of utils")
    try:
        with open(file_path,'rb') as f:
            obj = dill.load(f)
        logging.info("exited the load_object method of utils")
        return obj
    except Exception as e:
        raise USVisaException(e , sys) from e 
    

def save_numpy_array_data(file_path : str , array : np.array) -> None:
    """
    Saves numpy array data to file 
    :params file_path : str ocation of the file to save 
            array : np.array data to save
    """

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path , exist_ok=True)
        with open(file_path , 'wb') as f :
            np.save(f , array)
    except Exception as e:
        raise USVisaException(e , sys) from e 
    


def load_numpy_array_data(file_path : str) -> np.array :
    """
    load numpy array data from file 
    :params file_path : str location of file to load 
            return : np.array data loaded
    """

    try:
        with open(file_path , 'rb') as f:
            return np.load(f)
    except Exception as e:
        raise USVisaException(e , sys) from e 
    

def save_object(file_path : str , obj : object) -> None:
    logging.info("Etered the save_object method of utils")
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path , 'wb') as f:
            dill.dump(obj , f) 

        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise USVisaException(e , sys) from e 
    

def drop_columns(df : DataFrame , cols : list) -> DataFrame:
    """
    drop the columns from a pandas dataframe 
    :params df : pandas dataframe 
            cols : list of columns to be dropeed    
    """
    logging.info("entered drop_columns method of utils")
    try:
        df=df.drop(columns=cols,axis=1)
        logging.info("exited the drop_columns method of utils")
        return df 
    except Exception as e:
        raise USVisaException(e , sys) from e