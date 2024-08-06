from calendar import c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_driver_path = 'YOUR CHROME DRIVER PATH'

options = Options()
options.binary_location='/Applications/ChromiumDev.app/Contents/MacOS/Chromium'
#options.binary_location='/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get('https://www.python.org')
events_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget.last time')
events_name = driver.find_elements(By.CSS_SELECTOR, '.event-widget.last li a')


events = {}

for num in range(len(events_name)):
    events[num] = {
        "time": events_time[num].text,
        "name": events_name[num].text
    }




print(events)



driver.quit()

