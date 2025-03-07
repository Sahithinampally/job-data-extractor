# Utility functions

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def setup_chrome_driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Runs in background (no browser window)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    except Exception as e:
        print(f"Error setting up Chrome driver: {e}")
        return None

def extract_job_details(job):
    try:
        title = job.find_element(By.TAG_NAME, "h2").text.strip()
        company = job.find_element(By.CLASS_NAME, "text-sm.text-gray-500").text.strip()
        
        details = job.find_elements(By.CLASS_NAME, "ml-2")
        location = details[0].text.strip() if len(details) > 0 else "N/A"
        job_type = details[1].text.strip() if len(details) > 1 else "N/A"
        salary = details[2].text.strip() if len(details) > 2 else "N/A"
        category = details[3].text.strip() if len(details) > 3 else "N/A"
        job_link = job.get_attribute("href")

        return {
            "Title": title,
            "Company": company,
            "Location": location,
            "Job Type": job_type,
            "Salary": salary,
            "Category": category,
            "Job Link": job_link
        }
    except Exception as e:
        return None