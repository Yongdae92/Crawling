import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "MozillaMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}


url = "https://www.melon.com/chart/month/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")


soup = BeautifulSoup(html, 'html.parserd')