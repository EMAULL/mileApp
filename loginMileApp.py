from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://taskdev.mile.app/login")
driver.maximize_window()

org_input = driver.find_element(By.NAME, "organization")
org_input.send_keys("testonboard")
org_input.send_keys(Keys.ENTER)
time.sleep(5)

username_input = driver.find_element(By.NAME, "email or username")
username_input.send_keys("Test1234")

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Test1234")

driver.find_element(By.CSS_SELECTOR, "button.el-button--primary").click()

time.sleep(5)
message = driver.find_element(By.CSS_SELECTOR, "p.el-alert__description").text
assert "Login failed, please check your email or password." in message

driver.close()
