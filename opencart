from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.opencart.com/index.php?route=cms/demo")
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT,"Login").click()
