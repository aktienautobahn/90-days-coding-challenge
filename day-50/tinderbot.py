from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException 
# --------------------------------------------------

from time import sleep
import decimal

USER_NAME = "your username"
PASSWORD = "your password"


chrome_driver_path = 'YOUR CHROME DRIVER PATH'

options = Options()
options.binary_location='/Applications/ChromiumDev.app/Contents/MacOS/Chromium'

bot = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

bot.get('http://tinder.com')
sleep(5)
decline = bot.find_element(By.XPATH, '//*[@id="c464932099"]/div/div[2]/div/div/div[1]/div[2]/button/span')
decline.click()
sleep(3)
log_in = bot.find_element(By.XPATH, '//*[@id="c464932099"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in.click()
sleep(3)
facebook = bot.find_element(By.XPATH, '//*[@id="c-1263448977"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
facebook.click()

base_window = bot.window_handles[0]
facebook = False
while facebook == False:
    try:
        fb_login_window = bot.window_handles[1]
        bot.switch_to.window(fb_login_window)
        if bot.title == "Facebook":
            fb_username = bot.find_element(By.ID, 'email')
            fb_password = bot.find_element(By.ID, 'pass')
            fb_login_submit_button = bot.find_element(By.ID, 'loginbutton')
            fb_username.send_keys(USER_NAME)
            sleep(1)
            fb_password.send_keys(PASSWORD)
            sleep(1)
            fb_login_submit_button.click()
            sleep(1)
            facebook = True
        else:
            pass
    except NoSuchElementException:
        sleep(5)
        pass

start_tinder_success = False
while start_tinder_success == False:
    try:
        bot.switch_to.window(base_window)
        allow_location = bot.find_element(By.CSS_SELECTOR, '#c-1263448977 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$g-ds-background-brand-gradient\).button--primary-shadow.StyledButton.Bxsh\(\$bxsh-btn\).Fw\(\$semibold\).focus-button-style.W\(225px\).W\(a\).Mstart\(8px\)')
        allow_location.click()
        notification_disable = bot.find_element(By.XPATH, '//*[@id="c-1263448977"]/div/div/div/div/div[3]/button[2]')
        notification_disable.click()
        start_tinder_success = True

    except NoSuchElementException:
        sleep(5)
        pass

#clicker loop
for n in range(100):
    sleep(1)
    print(n)
    try:
        like_button1 = bot.find_element(By.XPATH, '//*[@id="c464932099"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button1.click()
    except ElementClickInterceptedException:
        try:
            match_popup = bot.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except:
            home_screen_not_interested = bot.find_element(By.CSS_SELECTOR, '#c-1263448977 > div > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\).Px\(24px\)--s > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(42px\)--s.Mih\(50px\)--ml.C\(\$c-secondary\).C\(\$c-base\)\:h.Fw\(\$semibold\).focus-button-style.D\(b\).Mx\(a\)')
            home_screen_not_interested.click()

    except NoSuchElementException:
        try:
            like_button2 = bot.find_element(By.XPATH, '//*[@id="c464932099"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
            like_button2.click()
            print('liked Button2')
            sleep(2)
        except NoSuchElementException:
            sleep(5)
            pass
    
    except:
        sleep(2)
        pass


bot.quit()