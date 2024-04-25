import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get("https://selfservicepreprod.mtn.ng/")

# Page Elements

footer = "div[class='hidden grid-cols-2 text-left md:grid lg:mb-0 lg:grid-cols-6 lg:text-left']"
breadcrumbContactus = "a[class='flex items-center text-sm font-normal text-[#000]']"
mailIcon = "img[alt='Mail']"
mailHeading = "div[class='relative mt-3 basis-[35%] rounded-lg bg-[#FFFAE0] p-4 md:mt-[30px] md:p-16'] div:nth-child(1) div h4"
mailParagraph = "div[class='relative mt-3 basis-[35%] rounded-lg bg-[#FFFAE0] p-4 md:mt-[30px] md:p-16'] div:nth-child(1) div p"
mailAnchorText = "div[class='relative mt-3 basis-[35%] rounded-lg bg-[#FFFAE0] p-4 md:mt-[30px] md:p-16'] div:nth-child(1) div a"
locationIcon = "img[alt='Location']"
locationHeading = "div[class='relative mt-3 basis-[35%] rounded-lg bg-[#FFFAE0] p-4 md:mt-[30px] md:p-16'] div:nth-child(2) div h4"
locationParagraph = "span[class='text-[14px] md:text-[15px] block font-normal text-[#29668B]']"
locationAnchorText = "div[class='relative mt-3 basis-[35%] rounded-lg bg-[#FFFAE0] p-4 md:mt-[30px] md:p-16'] div:nth-child(2) > span:nth-child(2)"
phoneIcon = "img[alt='Phone']"
phoneHeading = "div[class='relative mt-3 basis-[35%] rounded-lg bg-[#FFFAE0] p-4 md:mt-[30px] md:p-16'] div:nth-child(3) h4"
phoneCall300 = "div[class='relative mt-3 basis-[35%] rounded-lg bg-[#FFFAE0] p-4 md:mt-[30px] md:p-16'] div:nth-child(3) p a:nth-child(1)"
phoneCall080310300 = "div[class='relative mt-3 basis-[35%] rounded-lg bg-[#FFFAE0] p-4 md:mt-[30px] md:p-16'] div:nth-child(3) p a:nth-child(3)"
phoneTextdescription = "div[class='relative mt-3 basis-[35%] rounded-lg bg-[#FFFAE0] p-4 md:mt-[30px] md:p-16'] div:nth-child(3) p"
h4_mainTitle = "div[class='mt-[30px] basis-[60%]'] h4"
h3_mainTitle = "div[class='mt-[30px] basis-[60%]'] h3"
subTitle = "div[class='mt-[30px] basis-[60%]'] p"
firstName = "div[class='block flex-row items-center justify-between md:flex'] div:nth-child(1) label",
firstnamePlaceholder = "input[name='first_name']"
lastName = "div[class='block flex-row items-center justify-between md:flex'] div:nth-child(2) label"
lastnamePlaceholder = "input[name='last_name']"
phoneNumberLable = "div[class='flex flex-row items-center justify-between'] div:nth-child(1) label"
phoneNumberPlaceholder = "input[name='phone_no']"
emailLabel = "div[class='flex flex-row items-center justify-between'] div:nth-child(2) label"
emailPlaceholder = "input[name='email']"
subjectLable = "body > div:nth-child(1) > div:nth-child(2) > main:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(6) > label:nth-child(1)"
subjectPlaceholder = "input[name='subject']"
msgnote = "div[class='mt-5'] label:nth-child(1)"
msgBox = "textarea[placeholder='Type your text here..']"
submitButton = "button[type='submit']"
notification = "div[class='notification-container']"
noficationError = "div[class='notification notification-error notification-enter-done']"
notificationSuccess = "div[class='notification notification-success notification-enter-done']"
notificationTitle = ".title"

myExplicitWait = WebDriverWait(driver, 10, poll_frequency=2)
myExplicitWait.until(EC.presence_of_element_located((By.LINK_TEXT, "Contact us"))).click()
myExplicitWait.until(EC.presence_of_element_located((By.CSS_SELECTOR, firstnamePlaceholder))).send_keys("pankaj")

driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, lastnamePlaceholder).send_keys("Kahsyap")


time.sleep(2)
