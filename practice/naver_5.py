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

areas = soup.select(".view_wrap")

for i in areas :
    ad = i.select_one(".link_ad")
    if ad :
        continue
    else : 
        title = i.select_one(".title_link._cross_trigger")
        print(title.text)
        print(title["href"])
        print()
