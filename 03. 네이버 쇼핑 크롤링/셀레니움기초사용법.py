from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options = chrome_options)

# 웹페이지 해당 주소로 이동 
url = "https://shopping.naver.com/home"
driver.get(url)
driver.implicitly_wait(10)
search = driver.find_element(By.CSS_SELECTOR, "#__next > div > div.pcHeader_header__eETRe > div > div > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > div._gnbSearch_inner_2Zksb > div > input")
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)