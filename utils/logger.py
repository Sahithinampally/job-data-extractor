# Logging configuration

import logging
import os
from config.config import LOG_LEVEL

try:
    # Create the logs directory if it doesn't exist
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Set up logging
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(os.path.join(log_dir, "app.log")),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger()
except OSError as e:
    print(f"Error creating log directory: {e}")
except IOError as e:
    print(f"Error setting up logging: {e}")
except AttributeError as e:
    print(f"Error accessing logging attributes: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")