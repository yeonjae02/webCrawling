import requests
from bs4 import BeautifulSoup

response =requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") # 결과가 리스트
print(links)
print()

for link in links:
    title = link.text # 태그 안의 텍스트 요소를 가져옴
    url = link.attrs['href'] # href의 속성값을 가져옴
    print(title, url)