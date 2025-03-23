import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

# Create directory if it doesn't exist
download_dir = r"C:\AutoReport"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Set Chrome options to specify the download directory
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,  # Set custom download folder
    "download.prompt_for_download": False,  # Disable download prompt
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    # Disable the "Save As" dialog
    "plugins.always_open_pdf_externally": True,
    "profile.default_content_settings.popups": 0
}
chrome_options.add_experimental_option("prefs", prefs)

# Set up WebDriver (update path to ChromeDriver if needed)
driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=chrome_options)

try:
    # Open NSE website
    driver.get("https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%2050")
    
    # Wait for page to load completely
    time.sleep(5)
    
    # Locate the download button using the correct XPath
    download_button = driver.find_element(By.XPATH, '//*[@id="dwldcsv"]')
    
    # Scroll into view and click the button
    ActionChains(driver).move_to_element(download_button).perform()
    download_button.click()
    
    # Wait for download to complete (adjust time if needed)
    time.sleep(3)
    
    print(f"Download completed successfully to {download_dir}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    driver.quit()