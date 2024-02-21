from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# 옵션 설정
options = Options()
user = "User_Agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
options.add_argument(f'user-Agent={user}')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

# 크롤링 코드 작성
url = "https://kream.co.kr/"
driver.get(url)


driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(0.3)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)  #슈프림 끝에 \n으로도 가능
time.sleep(0.1)

for i in range(30):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    driver.save_screenshot("/Users/kwonyongdae/Desktop/oz_crawling/kream_screenshot/supreme.png")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")

num = 1
for i in items :
    product_name = i.select_one(".translated_name")
    if "후드" in product_name.text :
        brand = i.select_one(".product_info_brand.brand")
        price = i.select_one(".amount")
        # 넘버1부터 
        print(f'[{num}]')
        # 브랜드명 
        print(f'브랜드 : {brand.text}')
        # 제품명
        print(f'제품명 : ({product_name.text}')
        # 가격
        print(f'가격 : {price.text}')
        #print(i)
        print()
        num += 1
    

driver.quit()
