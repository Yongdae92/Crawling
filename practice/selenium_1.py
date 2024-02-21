from selenium import webdriver
from selenium.webdriver.common.by import By
f
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

url = "https://naver.com"

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

query = soup.select_one("#query")
print(query)