from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options with new 2024
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--disable-gpu")  # Applicable to windows os only
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

# Specify the path to chromedriver.exe (download and save on your computer)
service_obj = Service("C:\\Selenium_python\\drivers\\chromedriveWin64\\chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

