# Element Click actions/operations

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/buttons")
time.sleep(3)

# --- 3️⃣ Normal Click ---
normal_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
normal_btn.click()
print("✅ Normal Click Performed")

actions = ActionChains(driver)

# --- 4️⃣ Double Click ---
double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
actions.double_click(double_click_btn).perform()

# --- 5️⃣ Right Click (Context Click) ---
right_click_btn = driver.find_element(By.ID, "rightClickBtn")
actions.context_click(right_click_btn).perform()

# --- 6️⃣ Click and Hold (Long Press) ---
driver.get("https://demoqa.com/buttons")
time.sleep(2)

home_link = driver.find_element(By.LINK_TEXT, "Home")
actions.click_and_hold(home_link).pause(2).release().perform()

# --- 7 mouse hover ---
actions.move_to_element(normal_btn).perform()

time.sleep(3)

# 2️⃣ Open a Drag & Drop Demo Page
driver.get("https://demoqa.com/droppable")
time.sleep(2)

# 3️⃣ Locate Source (Draggable) and Target (Droppable) Elements
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

actions.drag_and_drop(source, target)
print("✅ Drag & Drop Performed")

time.sleep(3)

actions.click_and_hold(source).move_to_element(target).release().perform()
print("✅ Drag & Drop Performed (Alternative Method)")

time.sleep(3)

driver.close()
