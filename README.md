# Job Data Extractor

A web scraping project that extracts job listings from EdTech.com and saves them to an Excel file.

## Overview

This project uses Selenium WebDriver to scrape job listings from EdTech.com. It extracts relevant job details such as:

1. Title
2. Company
3. Location
4. Job type
5. Salary
6. Category
7. Job link

## Features

Scrapes job listings from EdTech.com
Extracts job details
Saves extracted data to an Excel file

## Usage

- Step 1: Clone the Repository  
  Bash  
  git clone https://github.com/Sahithinampally/job-data-extractor.git

- Step 2: Navigate to the Project Directory  
  Bash  
  cd job-data-extractor

* Step 3: Run the Script  
  Bash  
  python main.py

## File Descriptions

1. config.py: Stores configuration settings, such as the base URL, scroll pause time, and maximum scrolls.
2. webdriver.py: Sets up the Chrome WebDriver with the desired options.
3. scraper.py: Contains the logic for scrolling, extracting job listings, and parsing job details.
4. data.py: Handles data storage and conversion to a Pandas DataFrame.
5. utils.py: Provides utility functions for tasks like printing job details.
6. main.py: Serves as the entry point, orchestrating the scraping process.
7. README.md: Contains information about the project, its purpose, and usage instructions.

## Output

The script will output an Excel file named "EdTech_Jobs.xlsx" containing the extracted job listings.
