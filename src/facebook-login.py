from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

service_option = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service_option)
#driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

username = "sarkar.prodyot@gmail.com"

pwd = os.getenv("FB_PWD")

#print(os.environ("FB_PWD"))

username = driver.find_element(By.XPATH,"//input[@name='email']").send_keys(username)
#driver.find_element(By.XPATH,"//input[@name='pass']").send_keys(pwd)
#driver.find_element(By.CSS_SELECTOR,"button[name='login']").click()
time.sleep(2)