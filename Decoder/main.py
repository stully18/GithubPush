import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get(r"https://docs.google.com/forms/d/e/1FAIpQLSdAXtpgDK94DCA-b3V4jcGGeCR6a3dpgAeUU3HwgO6fNJYXgg/viewform")
driver.maximize_window()

def filloutform():
    motionInput= driver.find_element(by="xpath", value=r"""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input""")
    time.sleep(1)
    motionInput.send_keys("yes i do have motion")
    nameInput = driver.find_element(by="xpath", value=r"""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input""")
    time.sleep(1)
    nameInput.send_keys("look mom i know what im doing")
    time.sleep(1)
    submitButton = driver.find_element("xpath","//span[text()='Submit']")
    submitButton.click()
    submitAgainButton = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    submitAgainButton.click()
    time.sleep(1)
    filloutform()
filloutform()



