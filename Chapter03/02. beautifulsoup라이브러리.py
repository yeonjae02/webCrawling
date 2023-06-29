import requests
from bs4 import BeautifulSoup

# 서버에 대화 시도
response = requests.get("https://news.naver.com/")

# 서버에서 html을 줌
html = response.text

# html의 번역선생님으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')

# id값인 browserTitleArea인 것을 찾아냄.
word = soup.select_one('#browserTitleArea')

# 텍스트 요소만 출력
print(word.text)