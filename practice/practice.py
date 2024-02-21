from bs4 import BeautifulSoup
from selenium import webdriver
import time
base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")

search_url = base_url + keyword

driver = webdriver.Chrome()

driver.get(search_url)

time.sleep(3)

for i in range(5) :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

items = soup.select(".title_link")

for e, item in enumerate(items, 1):
    print(f"{e} : {item.text}")

driver.quit()