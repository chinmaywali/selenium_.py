from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")
driver.find_element(By.ID,"email").send_keys("asd@email.com")
driver.find_element(By.ID,"pass").send_keys("1234")

driver.find_element(By.NAME,"login").click()
driver.find_element(By.LINK_TEXT,"Try another way").click()
