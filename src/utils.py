import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        # Log the directory creation step
        dir_path = os.path.dirname(file_path)
        logging.info(f"Creating directory if not exists: {dir_path}")
        os.makedirs(dir_path, exist_ok=True)

        # Log the saving step
        logging.info(f"Attempting to save object to: {file_path}")
        
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        # Log successful save
        logging.info(f"Object saved successfully to: {file_path}")
        
    except Exception as e:
        # Log any errors during saving
        logging.error(f"Failed to save the object at {file_path}: {e}")
        raise CustomException(e, sys)






