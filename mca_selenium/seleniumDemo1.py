# 10 commonly used browser commands with Selenium WebDriver

import time
from selenium import webdriver

# get chrome driver
driver = webdriver.Chrome()

# 1. Opens google in the browser
driver.get("https://www.google.com")

# 2. Maximize current browser window
driver.maximize_window()
time.sleep(10)

# 3. Minimize current browser window
driver.minimize_window()

# 4. Navigate to Wikipedia
driver.get("https://www.wikipedia.org")
time.sleep(10)

# 5. Goes back to previous page
driver.back()

time.sleep(10)

# 6. Goes forward to next page
driver.forward()

time.sleep(10)

# 7. refresh the page
driver.refresh()
time.sleep(5)

# 8. Get title of current page
title = driver.title
print("title: ", title)

# 9. Get the current URl
current_url = driver.current_url
print("URL: ", current_url)

# 10. Get source code of current page
page_source = driver.page_source
# print("Source code: ", page_source)

# 11. Close the current browser tab
driver.close()

# 12. Closes all browser windows opened by selenium
driver.quit()