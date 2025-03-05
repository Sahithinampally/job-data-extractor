# Main program

import config
from utils import setup_chrome_driver, extract_job_details
from logger import logger

def main():
    logger.info("Starting job extraction")

    driver = setup_chrome_driver()
    driver.get(config.BASE_URL)

    job_list = []
    for _ in range(config.MAX_SCROLLS):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(config.SCROLL_PAUSE_TIME)
        
        jobs = driver.find_elements(By.XPATH, "//a[contains(@data-id, 'listing')]")
        for job in jobs:
            job_details = extract_job_details(job)
            if job_details:
                job_list.append(job_details)
                logger.info(f"Extracted: {job_details['Title']} | {job_details['Company']}")

    driver.quit()

    if job_list:
        df = pd.DataFrame(job_list)
        df.to_excel(f"output/{config.OUTPUT_FILE_NAME}", index=False, engine="xlsxwriter")
        logger.info(f"Job data saved to output/{config.OUTPUT_FILE_NAME}")
    else:
        logger.info("No job data found.")

if __name__ == "__main__":
    main()