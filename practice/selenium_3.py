from selenium import webdriver
from bs4 import BeautifulSoup
import time


header_user = {"User_Agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="

search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url
# req = request.get

driver = webdriver.Chrome()

driver.get(url)

time.sleep(3)

for i in range(5) :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

areas = soup.select(".view_wrap")
num = 1

for i in areas:
    ad = i.select_one(".link_ad")
    if ad :
        continue
    else :
        title = i.select_one(".title_link._cross_trigger")
        name = i.select_one(".user_info > a")
        print(num)
        print(f"글 제목 : {title.text}")
        print(f"글 작성자 : {name.text}")
        print(f"글 링크 : {title['href']}")
        print()

        num += 1

