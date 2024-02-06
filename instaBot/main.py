from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(2)

username_input = browser.find_element(by="xpath", value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
username_input.send_keys("mofot70899@namewok.com")
password_input = browser.find_element(by="xpath", value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
password_input.send_keys("easypie1234")
login_btn = browser.find_element(by="xpath", value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
login_btn.click()
sleep(5)
browser.close()
