from visa_approval.logger import logging 
from visa_approval.exception import USVisaException 
import sys


# logging.info("welcome to our firts custome log")
try :
    a = 1/ '1'
except Exception as e:
    logging.info( e)
    raise USVisaException(e , sys) from e