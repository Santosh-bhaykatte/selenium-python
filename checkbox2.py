from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com")

driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="HTML33"]/div[1]/input[1]').click()
driver.find_element(By.XPATH, '//*[@id="HTML33"]/div[1]/input[2]').click()
driver.find_element(By.XPATH, '//*[@id="HTML33"]/div[1]/input[3]').click()
