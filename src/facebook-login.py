from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import shutil
import tempfile 
import time
import os


options = Options()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')

# Create a temporary directory for the user data
user_data_dir = tempfile.mkdtemp()
options.add_argument(f"--user-data-dir={user_data_dir}")  # Use f-string

#service_option = Service("/home/ubuntu/chromedriver-linux64/chromedriver")
#driver = webdriver.Chrome(service=service_option)

#driver = webdriver.Chrome("/home/ubuntu/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

username = "sarkar.prodyot@gmail.com"

pwd = os.getenv("FB_PWD")

#print(os.environ("FB_PWD"))

username = driver.find_element(By.XPATH,"//input[@name='email']").send_keys(username)
#driver.find_element(By.XPATH,"//input[@name='pass']").send_keys(pwd)
#driver.find_element(By.CSS_SELECTOR,"button[name='login']").click()
time.sleep(2)
shutil.rmtree(user_data_dir)