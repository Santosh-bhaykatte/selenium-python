import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in")
driver.maximize_window()

time.sleep(5)

driver.get("https://omayo.blogspot.com")
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(4)

driver.refresh()
time.sleep(5)

driver.close()
