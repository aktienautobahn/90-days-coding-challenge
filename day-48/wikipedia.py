from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_driver_path = 'YOUR CHROME DRIVER PATH'

options = Options()
options.binary_location='/Applications/ChromiumDev.app/Contents/MacOS/Chromium'

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
articles_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')

print(articles_count.text)

driver.quit()
