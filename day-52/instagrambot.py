from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from decimal import Decimal
import os
from time import sleep
# --------------------------------------------------


# Get environment variables
USER = ''#os.getenv('IG_USER_NAME')
PASSWORD = ''#os.environ.get('IG_PASSWORD')




class InstaFollower:

    def __init__(self) -> None:
        chrome_driver_path = 'YOUR CHROME DRIVER PATH'

        options = Options()
        options.binary_location='/Applications/ChromiumDev.app/Contents/MacOS/Chromium'

        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(5)
        try:
            cookies = self.driver.find_element(By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm')
            cookies.click()
        except NoSuchElementException:
            pass
        username = self.driver.find_element(By.NAME, 'username')
        #username = self.driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
        password = self.driver.find_element(By.NAME, 'password')


        login_button = self.driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div')
        ActionChains(self.driver).move_to_element(username).click().perform()
        username.send_keys(USER)
        ActionChains(self.driver).move_to_element(password).click().perform()
        password.send_keys(PASSWORD)
        login_button.click()
        sleep(20)
        
        pass


    def find_followers(self):
        # not_loaded = True
        # while not_loaded:
        #     try:
        #         search_field = self.driver.find_element(By.CSS_SELECTOR, '#mount_0_0_o4 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div._a3gq._ab-1 > section > nav > div._acc1._acc3 > div > div > div._aawf._aawg > input')
        #         not_loaded = False
        #     except NoSuchElementException:
        #         self.driver.implicitly_wait(10)
        #         pass
        self.driver.get('https://www.instagram.com/simplemoney_ch/followers/')
        

        sleep(2)
        modal = self.driver.find_element('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            #In this case we're executing some Javascript, that's what the execute_script() method does. 
            #The method can accept the script as well as a HTML element. 
            #The modal in this case, becomes the arguments[0] in the script.
            #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)


    def follow(self):
        pass
         
instabot = InstaFollower()
instabot.login()
instabot.find_followers()