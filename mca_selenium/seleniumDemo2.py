# Window Actions

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.set_window_size(1200, 800)
driver.set_window_position(100, 50)

driver.get("https://www.google.com")

time.sleep(10)

driver.maximize_window()
driver.fullscreen_window()
time.sleep(10)



