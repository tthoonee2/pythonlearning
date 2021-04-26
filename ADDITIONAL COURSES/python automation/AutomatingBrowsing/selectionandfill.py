from selenium import webdriver
driver = webdriver.Edge('') #--> here you have to insert the path for the edge driver
driver.get('htps://www.seleniumeasy.com/test/basic-first-form-demo.html')
#the xpath is the best for automation
messagefield = driver.find_element_by_xpath('') #--> here you have to insert the xpath of the user
messagefield.send_keys('username')
messagebox = driver.find_element_by_xpath('') #---> here again
messagebox.click()

