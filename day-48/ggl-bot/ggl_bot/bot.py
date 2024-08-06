
import os
import sys
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.binary_location='/Applications/Chromium.app/Contents/MacOS/Chromium'
#options.binary_location='/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
#driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver', options=options)

class ggl():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver', options=options)
        
    def gglpop(self):
        self.driver.get("https://www.google.com")

        sleep(1)

        customise = self.driver.find_element_by_xpath('//*[@id="VnjCcb"]')
        customise.click()

        s_cust = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/button')
        s_cust.click()

        yt_cust = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div')
        yt_cust.click()

        ad_cust = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[5]/div[2]/div[2]/div/div[2]/div[1]/div/button')
        ad_cust.click()

        confirm = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/form/div/button')
        confirm.click()

        self.driver.get("https://www.google.com")

    def searching(self, kw):
        inputElems = self.driver.find_elements_by_css_selector('input[name=q]')

        for inputElem in inputElems:

	        inputElem.send_keys(kw)

	        # Presses Enter Key Like When You Press Enter Key to Search
	        inputElem.send_keys(Keys.ENTER)

    def results(self, pages):
        try:
            darkmode = self.driver.find_element_by_xpath('//*[@id="_nyz9YNnVLcvosAeml42YCw5"]/div/div[2]/div/span/svg/path')
            darkmode.click()
        except:
            pass
        
        results = []
        # noch die seiten überprüfen (anscheinend kehrt google zur ersten seite nach dem Klicken auf mehr als 10)
        for p in range(pages):
            
            #check on ommiting more results
            try:
                om = self.driver.find_element_by_xpath('//*[@id="ofr"]/i/a')
                
                om.click()
            except:
                pass
                
            for num in range(1,10):
                hlinks = self.driver.find_elements_by_xpath('//*[@id="rso"]/div[{}]/div/div/div[1]/a'.format(num))
                #snippet = self.driver.find_elements_by_xpath('//*[@id="rso"]/div[{}]/div/div/div[2]/a'.format(num))
                #titel = self.driver.find_elements_by_xpath('//*[@id="rso"]/div[{}]/div/div[2]/div[1]/a/h3'.format(num))
                
                for hlink in hlinks:
                    href = hlink.get_attribute('href')
                    #print(href)
                    results.append(href)
            
            self.nextpage()
        df = pd.DataFrame(results)
        
        #print(df)
        df.to_csv('results.csv',index=True)
                
            
    def nextpage(self):
        next_page = self.driver.find_element_by_xpath('//*[@id="pnnext"]')
        
        next_page.click()

    def scrolling(self):
        self.driver.execute_script("window.scrollTo(0, 1900)") 
