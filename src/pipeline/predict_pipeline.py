# src/pipeline/predict_pipeline.py

import os
import sys
from src.exception import CustomException
from src.utils import load_object
from src.pipeline.custom_data import CustomData  # Adjust the import

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join('artifacts', "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

            print(f"Loading model from: {model_path}")
            print(f"Loading preprocessor from: {preprocessor_path}")

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            print(f"Error in prediction pipeline: {str(e)}")
            raise CustomException(e, sys)
