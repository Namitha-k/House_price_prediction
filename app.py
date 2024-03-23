from housing.logger import logging
from housing.exception import HousingException
import sys

def print_even():
    try:
        logging.info("Start program")
        c = 2/0
        print(c)
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
    
print_even()