from twitterUserInfo import usarname,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

class Twitter:
    def __init__(self,usarname,password):
        
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("detach",True)
        self.browserProfile.add_experimental_option("prefs", {"intl.accept_Languages":"en,en_US"})
        self.browser = webdriver.Chrome()
        self.usarname = usarname
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(10)

        usarnameInput = self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        usarnameInput.send_keys(self.usarname)
        time.sleep(5)
        usarnameInput.send_keys(Keys.ENTER)
        time.sleep(5)
        
        #kişi giriş xpath aldık sonra ona ismi gönderdik
        
        #ileriye tıklattırdık
        passwordInput = self.browser.find_element("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        time.sleep(5)
        passwordInput.send_keys(self.password)
        time.sleep(5)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

    def search(self,hastag):
        searchInput = self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
        searchInput.send_keys(hastag)
        time.sleep(2)

        results = []

        list = self.browser.find_element(By.XPATH,"//div[@data-tesid='tweet']/div[2]/div[2]")
        time.sleep(2)
        print("count" + str(len(list)))

        for i in list:
            results.append(i.text)

        loopCounter = 0
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter >3:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter+=1
            
        list = self.browser.find_element(By.XPATH,"//div[@data-tesid='tweet']/div[2]/div[2]")
        time.sleep(2)
        print("count" + str(len(list)))

        for i in list:
            results.append(i.text) 

        with open("tweets.txt","w",encoding="UTF-8") as file:
            for item in results:
                file.write(f"{count}-{item}\n")
                count+=1

        list = self.browser.find_element(By.XPATH,"//div[@data-tesid='tweet']/div[2]/div[2]")
        
        count = 1
        for item in results:
            print(f"{count}-{item}")
            count+=1
            print("***********")

        
twitter = Twitter(usarname,password)

twitter.signIn()
twitter.search()