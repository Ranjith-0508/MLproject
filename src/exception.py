import sys
from src.logger import logging  # Importing the logger

def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  
    file_name = exc_tb.tb_frame.f_code.co_filename  
    error_message = "Error occurred in script: [{0}] at line number: [{1}] with message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))  
    return error_message  

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_detail=error_detail)   
        logging.error(self.error_message)  # Log the error message

    def __str__(self):
        return self.error_message

# Testing the custom exception
if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise ZeroDivisionError
    except Exception as e:
        logging.info("An error occurred before raising the custom exception.")
        raise CustomException(e, sys)  # Raise custom exception to log error



