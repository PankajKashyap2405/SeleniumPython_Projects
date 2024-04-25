from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://selfservicepreprod.mtn.ng/")
footer_container = "div[class='hidden grid-cols-2 text-left md:grid lg:mb-0 lg:grid-cols-6 lg:text-left']"

driver.implicitly_wait(10)
footerHolder = driver.find_element(By.CSS_SELECTOR, footer_container)
footerLinks = footerHolder.find_elements(By.TAG_NAME, "a")
print(len(footerLinks))

for link in footerLinks:
    footer_text = link.text
    #conidtional commands
    print("enable status ", link.is_enabled())
    print("enable status ",link.is_displayed())
    link.send_keys(Keys.CONTROL + Keys.ENTER)
    driver.switch_to.window(driver.window_handles[-1])
    print(footer_text + driver.title)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
