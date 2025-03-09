# Main program

from config import config
import time
from utils.logger import logger
from utils.utils import setup_chrome_driver, extract_job_details, By, pd
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from pandas.errors import EmptyDataError
import xlsxwriter.exceptions

def main():
    try:
        logger.info("Starting job extraction")

        driver = setup_chrome_driver()
        driver.get(config.BASE_URL)

        job_list = []
        for _ in range(config.MAX_SCROLLS):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(config.SCROLL_PAUSE_TIME)
                
                jobs = driver.find_elements(By.XPATH, "//a[contains(@data-id, 'listing')]")
                for job in jobs:
                    job_details = extract_job_details(job)
                    if job_details:
                        job_list.append(job_details)
                        logger.info(f"Extracted: {job_details['Title']} | {job_details['Company']}")
            except TimeoutException as e:
                logger.error(f"Timeout error occurred while scrolling or extracting jobs: {e}")
            except NoSuchElementException as e:
                logger.error(f"Element not found error occurred while extracting jobs: {e}")
            except WebDriverException as e:
                logger.error(f"Webdriver error occurred while scrolling or extracting jobs: {e}")


        driver.quit()
    except WebDriverException as e:
        logger.error(f"Webdriver error occurred while setting up or quitting webdriver: {e}")

    try:
        if job_list:
            df = pd.DataFrame(job_list)
            try:
                df.to_excel(f"output/{config.OUTPUT_FILE_NAME}", index=False, engine="xlsxwriter")
                logger.info(f"Job data saved to output/{config.OUTPUT_FILE_NAME}")
            except EmptyDataError as e:
                logger.error(f"Error saving job data to Excel: DataFrame is empty - {e}")
            except xlsxwriter.exceptions.FileCreateError as e:
                logger.error(f"Error saving job data to Excel: Unable to create file - {e}")
        else:
            logger.info("No job data found.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()