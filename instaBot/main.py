from time import sleep
from selenium import webdriver


browser = webdriver.Firefox()
browser.implicitly_wait(5)


class LoginPage:
    def __init__(self,browser):
        self.browser = browser
    def login(self):
        username_input = browser.find_element(by="xpath", value="input[name='username']")
        username_input.send_keys("mofot70899@namewok.com")
        password_input = browser.find_element(by="xpath", value="input[name='password']")
        password_input.send_keys("easypie1234")
        login_btn = browser.find_element(by="xpath", value="//button[@type='submit']")
        login_btn.click()
        sleep(5)

class HomePage:
    def __init__(self,browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')
    def go_to_login_page(self):
        self.browser.find_element(type="xpath", value="//a[text()='Log in']").click()
        sleep(2)
        return LoginPage(self.browser)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login()

