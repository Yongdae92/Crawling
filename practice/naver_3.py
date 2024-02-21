import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "MozillaMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

# 접속하고자 하는 주소 입력 => url
base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url
req = requests.get(url, headers=header_user)


html = req.text
soup = BeautifulSoup(html, "html.parser")

titles = soup.select(".news_tit")
n = 1
for i in titles :
    print(f'{n}번 뉴스')
    title = i.text
    print(f'뉴스 제목 : {title}')
    print(f'뉴스 링크 : {i['href']}')
    print()
    n += 1