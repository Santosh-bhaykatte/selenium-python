# Form Actions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 1️⃣ Launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

# 2️⃣ Open a sample form page
driver.get("https://www.w3schools.com/html/html_forms.asp")

time.sleep(2)

# --- 3️⃣ Access and Fill Text Input ---
# Locate the "First name" field and type text
first_name = driver.find_element(By.NAME, "fname")
first_name.clear()
first_name.send_keys("John")

# Locate the "Last name" field and type text
last_name = driver.find_element(By.NAME, "lname")
last_name.clear()
last_name.send_keys("snow")

# --- 4️⃣ Access and Click a Radio Button ---
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_input_radio")
driver.switch_to.frame("iframeResult")
male_radio = driver.find_element(By.XPATH, "//input[@value='male']")
male_radio.click()

# --- 5️⃣ Access and Click a Checkbox ---
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_input_checkBox")
driver.switch_to.frame("iframeResult")
vehicle_checkbox = driver.find_element(By.XPATH, "//input[@value='bike']")
vehicle_checkbox.click()

# --- 7️⃣ Click Submit Button ---
submit_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_btn.click()

# Wait to see result before closing
time.sleep(3)

# 8️⃣ Close Browser
driver.quit()