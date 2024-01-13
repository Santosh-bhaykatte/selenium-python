from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com")
driver.maximize_window()

driver.find_element(By.ID, 'uploadfile').send_keys("C:\\Users\\HP\\Desktop\\Akash11.docx")


