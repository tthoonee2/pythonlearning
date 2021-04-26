from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.chrome()
driver.maximize_window()
driver.get('') # --> insert link of the html page to be retriveved
source = driver.find_element_by_xpath('') #--> #insert xpath of the object to be moved
dest = driver.find_element_by_xpath('') #destination xpath
#now we add a chain of actions
actions = ActionChains(driver)
actions.drag_and_drop(source,dest).perform() #this executes the command from source to dest

