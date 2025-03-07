# Configuration file

import logging

# Base URL for job listings
BASE_URL = "https://www.edtech.com/jobs"

# Scroll and load all jobs
SCROLL_PAUSE_TIME = 4  # Time to wait after scrolling
MAX_SCROLLS = 20  # Prevent infinite loops

# Output file name
OUTPUT_FILE_NAME = "EdTech_Jobs.xlsx"

# Logging configuration
LOG_LEVEL = logging.ERROR
LOG_FILE_NAME = "app.log"
