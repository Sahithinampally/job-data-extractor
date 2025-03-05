#Job Data Extractor
A web scraping project that extracts job listings from EdTech.com and saves them to an Excel file.
##Overview
This project uses Selenium WebDriver to scrape job listings from EdTech.com. It extracts relevant job details such as title, company, location, job type, salary, category, and job link.
##Features
Scrapes job listings from EdTech.com
Extracts job details such as title, company, location, job type, salary, category, and job link
Saves extracted data to an Excel file
##Usage
Clone the repository: git clone https://github.com/Sahithinampally/job-data-extractor.git
Navigate to the project directory: cd job-data-extractor
Run the script: python main.py
##File Descriptions
config.py: Stores configuration settings, such as the base URL, scroll pause time, and maximum scrolls.
webdriver.py: Sets up the Chrome WebDriver with the desired options.
scraper.py: Contains the logic for scrolling, extracting job listings, and parsing job details.
data.py: Handles data storage and conversion to a Pandas DataFrame.
utils.py: Provides utility functions for tasks like printing job details.
main.py: Serves as the entry point, orchestrating the scraping process.
README.md: Contains information about the project, its purpose, and usage instructions.
##Output
The script will output an Excel file named "EdTech_Jobs.xlsx" containing the extracted job listings.
