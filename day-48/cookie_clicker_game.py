from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# --------------------------------------------------

import time
import decimal


chrome_driver_path = 'YOUR CHROME DRIVER PATH'

options = Options()
options.binary_location='/Applications/ChromiumDev.app/Contents/MacOS/Chromium'

bot = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

bot.get('http://orteil.dashnet.org/experiments/cookie/')

# for _ in range(100):


#     print(int(bot.find_element(By.ID, 'buyPortal').text.split()[2].replace(',','')))


store = bot.find_elements(By.CSS_SELECTOR, '#store div')
store_elements = [element.get_attribute('id') for element in store]

# defining main objects
cookie = bot.find_element(By.ID, 'cookie')
money = bot.find_element(By.ID, 'money')


timeout = time.time() + 5
one_min = time.time() + 60
five_min = time.time() + 60*5
minute = 0

# buying in store function
def store():
    price_list = {}
    for element_name in store_elements:
        if bot.find_element(By.ID, element_name).get_attribute('class') == "":

            item = {bot.find_element(By.ID, element_name).get_attribute('id'):int(bot.find_element(By.ID, element_name).text.split()[2].replace(',',''))}
            price_list.update(item)


    for item_id in reversed(price_list):

        if int(money.text.replace(',','')) >= price_list.get(item_id):
            try:
                bot.find_element(By.ID, item_id).click()
            except:
                pass

#main part  -  while loop
continue_clicking = True
while continue_clicking:
    cookie.click()

    if time.time() > timeout:
        timeout += 15
        store()
    if time.time() >= one_min:
        one_min += 60
        minute += 1
        print(f'Minute from start: {minute}')

    if time.time() > five_min:
        continue_clicking = False

#get cookies per second after the end of the while loop
cookies_per_second = decimal.Decimal(bot.find_element(By.ID, "cps").text.split(':')[1].strip())
print(f'Your cookies/sec result is: {cookies_per_second}')