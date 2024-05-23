from Sensor.exception import SensorException
import os
import sys
import logging
from datetime import datetime

# Define the log file name based on the current datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log file path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Corrected this line
)

# Example usage
logging.info("Logging setup complete.")

# Function to test custom exception handling
def test_exception():
    try:
        a = 1 / 0  # This will raise a division by zero error
    except Exception as e:
        raise SensorException(e, sys)  # Raise custom exception with original error and system info

# Main execution block
if __name__ == "__main__":
    try:
        test_exception()  # Call the test function
    except SensorException as se:
        logging.error(se)  # Log the custom exception
        print(se)  # Optionally, print the custom exception to the console
