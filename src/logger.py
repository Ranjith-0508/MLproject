import logging
import os
from datetime import datetime

# Set up the log file path
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")  # 'logs' directory in current working directory
os.makedirs(logs_dir, exist_ok=True)  # Create logs directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Print the path where the log file should be saved
print(f"Log file path: {LOG_FILE_PATH}")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# Add console handler to also output to the console
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(console_handler)
