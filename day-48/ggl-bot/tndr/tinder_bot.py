import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import csv


options = Options()
options.binary_location='/Applications/Chromium.app/Contents/MacOS/Chromium'
#options.binary_location='/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
#driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver', options=options)

#import cookies: try out different solutions
""" 
reader = csv.reader(open('cookies_tinder.csv', 'r'))
d = {}
for row in reader:
   k, v = row
   d[k] = v

#setting cookies in requests:
Next, set those cookies in requests:

s = requests.Session()
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])
//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/div/div[4]/button

#c2094796203 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.profileCard.Pos\(r\).D\(f\).Ai\(c\).Fxd\(c\).Expand--s.Mt\(a\) > div.Pos\(f\).W\(100\%\).B\(0\).Z\(1\).Pe\(n\).Pos\(a\)--ml.Bdrsbend\(8px\)--ml.Bdrsbstart\(8px\)--ml.Bg\(\$transparent-white-gradient\) > div > div > div:nth-child(4) > button
#c2094796203 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.profileCard.Pos\(r\).D\(f\).Ai\(c\).Fxd\(c\).Expand--s.Mt\(a\) > div.Pos\(f\).W\(100\%\).B\(0\).Z\(1\).Pe\(n\).Pos\(a\)--ml.Bdrsbend\(8px\)--ml.Bdrsbstart\(8px\)--ml.Bg\(\$transparent-white-gradient\) > div > div > div:nth-child(4) > button

 """
cookie_dict ={}

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver', options=options)
        #remember base window
        base_window = self.driver.window_handles[0]

    def reconnect(self):
        self.driver.switch_to_window('CDwindow-BA4957B3EFA0313CFA63512B39861890') # not working yet
    
    # Adds a cookie to your current session.
    def add_cookies(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def set_cookies(cookies, s):
        for cookie in cookies:
            if 'httpOnly' in cookie:
                httpO = cookie.pop('httpOnly')
                cookie['rest'] = {'httpOnly': httpO}
            if 'expiry' in cookie:
                cookie['expires'] = cookie.pop('expiry')
            s.cookies.set(**cookie)
        return s
    
    def cookies(self):
        self.driver.get_cookies()

    def popupwindow(self):
        self.driver.switch_to_window(self.base_window)

    def login(self):
       self.driver.get("https://www.tinder.com")
       #lg_btn = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
    
    def like(self):
        try:
            like_btn_fold = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
            like_btn_fold.click()                              
        except Exception:
            try:
                like_btn_unfold = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/div/div[4]/button')
                like_btn_unfold.click()
            except Exception:
                try:
                    like_btn_rest = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
                    like_btn_rest.click()
                except Exception:
                    try:
                        like_btn_rest = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
                        like_btn_rest.click()
                    except Exception:
                            like_btn_rest = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
                            like_btn_rest.click()       

                                 
    def dislike(self):
        try:
            dislike_btn_fold = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
            dislike_btn_fold.click()
        except Exception:
            try: 
                dislike_btn_unfold = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/div/div[2]/button')
                dislike_btn_unfold.click()
            except Exception:
                try:
                    dislike_btn_rest = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
                    dislike_btn_rest.click()
                except Exception:
                    try:
                        dislike_btn_rest = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
                        dislike_btn_rest.click()
                    except Exception:
                            like_btn_rest = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
                            like_btn_rest.click()       


    
    
    
    def close_popup(self):
        try:
            self.maybe_later()
        except Exception:
            self.home_screen_popup()


        #self.driver.switch_to_window(self.driver.window_handles[1])
        #bot.driver.switch_to_window(bot.driver.window_handles[0])

    def auto_swipe(self):
        i = 0
        while True:
            sleep(2)
            try:
                self.like()
                i = i + 1
                print(i)

                if i > 50:
                    proceed = input('Already liked {} profiles. Proceed? y/n'.format(i),)
                    if proceed == "y":
                        pass
                    else:
                        break

            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()              



    def maybe_later(self):
        maybe_later = self.driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/button[2]')
        maybe_later.click()
    
    def location_popup(self):
        loc_popup_allow = self.driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div/div/div[3]/button[1]')
        loc_popup_allow.click()

    def home_screen_popup(self):
        not_interested = self.driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div[2]/button[2]')
        not_interested.click()

    #get info of profile
    def info(self): #manchmal gibt es kein Age und Verified! Exceptions einbauen!

        try:
            name_profil_fold = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[1]/div/div[1]/span')
            name = name_profil_fold.get_attribute('innerHTML')

            age_profil_fold = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[1]/div/span[2]')
            age = age_profil_fold.get_attribute('innerHTML')
            
            verified_fold = self.driver.find_element_by_xpath('//*[@id="5a34dadd668a1706"]')
            verified      = verified_fold.get_attribute('innerHTML')
        except:
            name_profil_unfold =      self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/h1')
            name = name_profil_unfold.get_attribute('innerHTML')

            age_profil_unfold = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/span')
            age = age_profil_fold.get_attribute('innerHTML')

            verified_unfold = self.driver.find_element_by_xpath('//*[@id="3ca3a83845a7c527"]')
            verified      = verified_fold.get_attribute('innerHTML')

        return name, age, verified

    def headers(self): #hier erschien HTML Text mit Spotify composition
        n = 1
        headers = []
        while True:
            try:
                r = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[2]/div/div/div[{}]/div[2]'.format(n))
                row = r.get_attribute('innerHTML')
                headers.append(row)
                n = n + 1
            except:
                break
        return headers

    def description(self):
        try:
            descr_profil_fold =  self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[2]/div/div')
            descr = descr_profil_fold.get_attribute('innerHTML')

        except:
            descr_profil_unfold  = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div')
            descr = descr_profil_unfold.get_attribute('innerHTML')
        return descr

    
    def passions(self):  # hier erschien HTML Text mit next profile name 
        n = 1
        passions = []
        while True:
            try:                
                p = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/div/div[{}]'.format(n))
                passion = p.get_attribute('innerHTML')
                passions.append(passion)
                n = n + 1
            except:
                break
        return passions
               
    
    def unfold(self):
        info_btn = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/button')
        info_btn.click()

    def fold_back(self):
        info_btn = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a')
        info_btn.click()
    
    def next_person(self):
        next_name = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/div[1]/span')
        name_np = next_name.get_attribute('innerHTML')
        next_age = self.driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[1]/div/span[2]')
        age = next_age.get_attribute('innerHTML')
        
        return name_np, age

    def next_pic(self):
        #put here code
        return self
