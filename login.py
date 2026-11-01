
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open HTML login page
driver.get("file:///D:/agile_lab_prac/login.html")

# Enter username
driver.find_element(By.ID, "username").send_keys("admin")

# Enter password
driver.find_element(By.ID, "password").send_keys("1234")

# Click login button
driver.find_element(By.ID, "login").click()

time.sleep(2)

# Check login result
message = driver.find_element(By.ID, "message").text

print("Result:", message)

assert message == "Login Successful!"

print("Login Test Passed!")

driver.quit()
