from numpy import sign
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from decimal import Decimal
# --------------------------------------------------

from time import sleep


USER_NAME = ""
PASSWORD = ""

PROMISED_DOWN = 150
PROMISED_UP = 10



class InternetSpeedTwitterBot:

    def __init__(self) -> None:
        chrome_driver_path = 'YOUR CHROME DRIVER PATH'

        options = Options()
        options.binary_location='/Applications/ChromiumDev.app/Contents/MacOS/Chromium'

        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        sleep(3)
        go = self.driver.find_element(By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a > span.start-text')
        go.click()
        sleep(60)
        self.down = Decimal(self.driver.find_element(By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span').text)
        self.up = Decimal(self.driver.find_element(By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span').text)
        pass

    def tweet_at_provider(self):
        self.driver.get('https://www.twitter.com')
        sleep(5)
        try:
            sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        except NoSuchElementException:
            sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[2]/div[4]/div[2]/span/span')
        finally:
            sign_in.click()
        sleep(2)
        user = self.driver.find_element(By.CSS_SELECTOR, '#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input')
        user.send_keys(USER_NAME)
        sleep(2)
        next_button = self.driver.find_element(By.CSS_SELECTOR, '#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6)')
        next_button.click()
        self.driver.implicitly_wait(10)
        sleep(2)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        sleep(2)
        try:
            next_button = self.driver.find_element(By.CSS_SELECTOR, '#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div > span > span')
            next_button.click()
        except NoSuchElementException:
            login = self.driver.find_element(By.CSS_SELECTOR, '#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div > div > span > span')
            login.click()
        self.driver.implicitly_wait(5)
        sleep(2)

        self.driver.get("https://twitter.com/compose/tweet")
        sleep(3)
        actions = ActionChains(self.driver)
        actions.send_keys(f"Hey Internet Provider, why is my internet speed {bot.down}down/{bot.up}up when I pay for 100down/10up?")
        actions.send_keys(Keys.ENTER)
        actions.perform()
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_button.click()
        print('Twitted successfully')

    


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < 100 or bot.up < 10:
    bot.tweet_at_provider()

print(f'Download speed: {bot.down.text}')
print(f'Upload speed: {bot.up.text}')


