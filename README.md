# **job-data-extractor**  

A web scraping project that extracts job listings from EdTech companies using **Selenium** and **Python**.  

## **Description**  

This project automates the extraction of **job listings** from various **EdTech companies**. It gathers essential details such as:  
- **Job Title**  
- **Company Name**  
- **Location**  
- **Job Type**  
- **Salary** (if available)  
- **Category**  
- **Job Link**  

The scraped data is saved in an **Excel file** for further analysis.  

## **Features**  

- Scrapes job listings from EdTech companies  
- Extracts key job details  
- Saves data to an **Excel file**  
- Organizes files into structured folders  

## **Project Structure**  

```sh

EdTech-Job-Scraper/
│── config/            # Configuration files  
│   └── config.py      # Configuration settings  
│── utils/             # Utility files  
│   ├── logger.py      # Logging configuration  
│   └── util.py        # Utility functions  
│── main.py            # Main script  
│── requirements.txt   # Project dependencies  
│── logs/              # Log files  
│── output/            # Scraped data output files  
│── README.md          # Project documentation

   ```

## **Requirements**  

Ensure you have **Python 3.x** installed. The following dependencies are required:  
- **selenium**  
- **pandas**  
- **webdriver-manager**  

## **Installation & Usage**  

### **1. Clone the Repository**  

```sh
git clone https://github.com/your-username/EdTech-Job-Scraper.git
cd EdTech-Job-Scraper
   ```
### **2. Install Dependencies**

```sh
pip install -r requirements.txt
python src/main.py
   ```

### **3. Run the Scraper**

```sh
python src/main.py
   ```

### **Output**
The scraped job data will be saved as:
📁 output/EdTech_Jobs.xlsx

### **Contributing**
Contributions are welcome! 🚀
If you'd like to contribute:

- Fork the repository
- Make your changes
- Submit a pull request

License
This project is licensed under the MIT License.
