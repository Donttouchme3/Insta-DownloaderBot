from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
import os
import time

load_dotenv()
Options = webdriver.ChromeOptions()
Options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70')
Options.add_argument('--headless')
Driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options)


def GetLink(Link):
    Driver.get(os.getenv('URL'))
    time.sleep(1)
    Input = Driver.find_element(By.NAME, 'sf_url')
    Input.send_keys(Link)
    Input.send_keys(Keys.ENTER)
    time.sleep(8)
    DownloadButton = Driver.find_elements(By.CLASS_NAME, 'download-icon')
    ContentUrls = []
    for i in DownloadButton:
        ContentUrls.append(i.get_attribute('href'))
    return ContentUrls
    Driver.close()
    Driver.quit()




