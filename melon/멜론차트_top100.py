import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "MozillaMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}


url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

chart50 = soup.select(".lst50")
chart100 = soup.select(".lst100")
chart = chart50 + chart100


for chart, i in enumerate(chart, 1):
    title = i.select_one(".ellipsis.rank01 a")
    singer = i.select_one(".ellipsis.rank02 a")
    album = i.select_one(".ellipsis.rank03 a")
    rank = i.select_one(".rank_wrap > span:nth-child(2)")
    rankUpDown = i.select_one(".rank_wrap > span:nth-child(2)").get("class")[0]

    print(f"순위 : {chart}")
    print(f"제목: {title.text}")
    print(f"가수 : {singer.text}")
    print(f"앨범 : {album.text}")
    if rankUpDown == "up" : 
        print(f"단계상승 : {rank.text}")
    elif rankUpDown == "down" :
        print(f"단계하락 : {rank.text}")
    else :
        pass
    print()