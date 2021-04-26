#explicit wait function vs implicit wait function
#we do the explicit wait functions
#we are working around the method of ajax
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = 'https://www.google.com/earth/' #this is an example of an url which uses ajax to load things separately with
# timings
driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)
launchbutton = wait.until(EC.element_to_be_clickable((By.xpath, ''))) #waits for the element to be clickable and the el-
# ement is indicated as xpath
launchbutton.click





