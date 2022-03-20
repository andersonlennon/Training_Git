import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://www.google.com")
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("Testando")
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()
