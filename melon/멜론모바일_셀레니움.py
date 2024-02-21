from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# 옵션 설정
options = Options()
user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"
# options.add_argument(f'User-Agent={user}')
options.add_argument('user-agent=' + user)

options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options = options)




# 크롤링 코드 작성
url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(2)

if driver.current_url != url :
    driver.get(url)
    time.sleep(2)

driver.find_element(By.LINK_TEXT, "닫기").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(2)

more_btn = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()

# 노래 순위
# 노래 제목
# 가수 이름