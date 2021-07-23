import os
from selenium import webdriver
from selenium.webdriver.commom.keys import Keys
driver=webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.current_url)
print(driver.title)

