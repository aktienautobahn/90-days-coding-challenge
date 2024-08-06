from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_driver_path = 'YOUR CHROME DRIVER PATH'

options = Options()
options.binary_location='/Applications/ChromiumDev.app/Contents/MacOS/Chromium'

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get('path')
f_name = driver.find_element(By.NAME, 'fName')
l_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
sign_up_button = driver.find_element(By.TAG_NAME, 'button')

f_name.send_keys("FakeName")
l_name.send_keys("FakeName")
email.send_keys("fakeEmail@email.com")
sign_up_button.send_keys(Keys.ENTER)
