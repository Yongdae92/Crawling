import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "MozillaMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

# 접속하고자 하는 주소 입력 => url
base_url = "https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query="
search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

title = soup.select(".title_link._cross_trigger")
name = soup.select(".user_info > a")



for i in zip(title, name):
    print(i)
    
    print(f'블로그 제목 : {i[0].text}')
    print(f'블로그 작성자 : {i[1].text}')
    print(f'블로그 링크 : {i[0]['href']}')
    print()

    