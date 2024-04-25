from selenium import webdriver
from selenium.webdriver.common.by import By

#paste webdriver in Scripts folder in python folder, Trick
driver = webdriver.Edge()
driver.get("https://money.rediff.com/gainers")
textValue = driver.find_element(By.XPATH,"//tbody/tr[3]").text
print(textValue)





