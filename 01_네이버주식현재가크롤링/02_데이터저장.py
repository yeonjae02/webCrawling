import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'C:\startcoding\01_네이버주식현재가크롤링\data.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화된 시트 선택
# 종목 코드 리스트
codes = [
    '005930',
    '000660',
    '035720'
]

row = 2
for code in codes:
  url = f"https://finance.naver.com/item/sise.naver?code={code}"
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  price = soup.select_one("#_nowVal").text
  price = price.replace(',', '') # 숫자 내 , 제거
  print(price)
  ws[f'B{row}'] = int(price)
  row += 1

wb.save(fpath)