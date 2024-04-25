import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#paste webdriver in Scripts folder in python folder, Trick
driver = webdriver.Edge()
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
textValue = driver.find_element(By.XPATH,"//tbody/tr[3]/td[1]/a")
#difference between text (its for inner text) and get_attribute (it's for attribute text'
print(textValue.text)
print(textValue.get_attribute('href'))
textValue.click()

time.sleep(5)
driver.back()
time.sleep(2)
driver.forward()
driver.refresh()
#browser commands
print(driver.title)
print(driver.current_url)
print(driver.page_source)
#conditional Commands




