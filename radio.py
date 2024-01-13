import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com")

driver.maximize_window()
# ++++++++++++++++++++++++++++++

radio1 = driver.find_element(By.ID, 'radio1')

if radio1.is_selected():
    pass
else:
    radio1.click()

time.sleep(5)

radio2 = driver.find_element(By.ID, 'radio2')

if radio2.is_selected():
    pass
else:
    radio2.click()
