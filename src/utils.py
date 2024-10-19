import os
import sys
import numpy as np 
import pandas as pd
import dill
import pickle

from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

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
        logging.error(f"Failed to save the object at {file_path}: {str(e)}")
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model_name = list(models.keys())[i]  # Add this line to define model_name
            model = models[model_name]
            para = param[model_name]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            logging.info(f"Best parameters for {model_name}: {gs.best_params_}")

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        logging.error(f"Error in model evaluation: {str(e)}")
        raise CustomException(e, sys)
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)







