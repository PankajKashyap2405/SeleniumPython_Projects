from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode

service_obj = Service("C:\\Selenium_python\\drivers\\chromedriveWin64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input[placeholder=Password]").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click() #'' not required

actual_title = driver.title
expt_title = "OrangeHRM"
if actual_title == expt_title:
    print("Login test pass")
else:
    print("Login test fail")

driver.close()
