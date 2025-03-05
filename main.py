from webdriver import setup_webdriver
from scraper import extract_job_listings, parse_job_details
from data import convert_to_dataframe
from config import BASE_URL, SCROLL_PAUSE_TIME, MAX_SCROLLS
import time

def main():
    driver = setup_webdriver()
    driver.get(BASE_URL)

    # Scroll and load all jobs
    job_list = []
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(MAX_SCROLLS):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("Reached end of job listings.")
            break
        last_height = new_height

    jobs = extract_job_listings(driver)
    print(f"Total Jobs Found: {len(jobs)}")

    for job in jobs:
        try:
            job_details = parse_job_details(job)
            job_list.append(job_details)
            #print(f"Extracted: {job_details['Title']} | {job_details['Company']} | {job_details['Location']} | {job_details['Job Type']} | {job_details['Salary']} | {job_details['Category']}")
        except Exception as e:
            print(f"Error extracting job: {e}")

    driver.quit()

    if job_list:
        df = convert_to_dataframe(job_list)
        df.to_excel("EdTech_Jobs.xlsx", index=False, engine="xlsxwriter")
        print("✅ Job data saved to EdTech_Jobs.xlsx")
    else:
        print("❌ No job data found.")

if __name__ == "__main__":
    main()