import logging
import os
from datetime import datetime

# Print the current working directory to verify where the logs folder will be created
print(f"Current working directory: {os.getcwd()}")

# Create the log file name with a .log extension and correct the date format
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs directory path and print it for debugging
logs_path = os.path.join(os.getcwd(), "logs")
print(f"Logs folder path: {logs_path}")

# Try creating the directory and handle any errors
try:
    os.makedirs(logs_path, exist_ok=True)
    print("Logs folder created successfully.")
except Exception as e:
    print(f"Error creating logs folder: {e}")

# Define the full path for the log file inside the logs directory
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logger to write to the specified log file with proper format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Log a sample message to confirm logging has started
if __name__ == "__main__":
    logging.info("Logging has started")
    print(f"Log file created at: {LOG_FILE_PATH}")
