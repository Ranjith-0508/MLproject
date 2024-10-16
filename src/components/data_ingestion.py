import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'src'))
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation, DataTransformationConfig
print(DataTransformation)

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Correct the file path if necessary
            df = pd.read_csv(r'notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            # Log the paths where the data will be saved
            logging.info(f"Train data will be saved at: {self.ingestion_config.train_data_path}")
            logging.info(f"Test data will be saved at: {self.ingestion_config.test_data_path}")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved at: {self.ingestion_config.raw_data_path}")

            # Split the dataset into train and test sets
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test sets to their respective paths
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train and test data saved successfully.")

            # Log confirmation that the files are saved
            logging.info(f"Train data saved at: {self.ingestion_config.train_data_path}")
            logging.info(f"Test data saved at: {self.ingestion_config.test_data_path}")

            logging.info("Ingestion of the data is completed")

            # Returning the paths to train and test data
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    # Step 1: Initiate Data Ingestion
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    # Step 2: Log before calling DataTransformation
    logging.info("Calling DataTransformation to process data.")
    
    # Step 3: Call DataTransformation to process the train and test data
    data_transformation = DataTransformation()
    train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data, test_data)

    # Add log to confirm that data transformation is about to begin
    logging.info(f"Calling initiate_data_transformation with train file: {train_data} and test file: {test_data}")
    
    # This will start the data transformation process
    data_transformation.initiate_data_transformation(train_data, test_data)
    
    # Log after data transformation is completed (optional)
    logging.info(f"Data transformation completed, preprocessor saved at: {preprocessor_path}")

