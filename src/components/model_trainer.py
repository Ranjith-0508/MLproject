import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        logging.info("Initializing ModelTrainer.")
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Starting model training process.")
            
            # Split train and test arrays
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            logging.info("Splitting training and test data successfully.")

            # Define models to evaluate
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            logging.info(f"Evaluating models: {list(models.keys())}")

            # Evaluate models and get the report
            model_report = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models)
            logging.info(f"Model report: {model_report}")

            # Get the best model score
            best_model_score = max(sorted(model_report.values()))

            # Get the best model name
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            logging.info(f"Best model: {best_model_name} with score: {model_report[best_model_name]}")

            if best_model_score < 0.1:
                raise CustomException("No suitable model found.")

            # Save the best model
            save_object(self.model_trainer_config.trained_model_file_path, best_model)
            logging.info(f"Model saved successfully at {self.model_trainer_config.trained_model_file_path}")

            # Predict and calculate R2 score on the test set
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)

            logging.info(f"Model R2 score: {r2_square}")

            return r2_square

        except Exception as e:
            logging.error(f"Error in model training: {str(e)}")
            raise CustomException(e, sys)


