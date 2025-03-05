from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_job_listings(driver):
    jobs = driver.find_elements(By.XPATH, "//a[contains(@data-id, 'listing')]")
    return jobs

def parse_job_details(job):
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