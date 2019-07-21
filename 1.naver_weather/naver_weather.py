from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

soup = bs(html.text, 'html.parser')
pprint(type(soup))
data1 = soup.find('div', {'class':'detail_box'})
#pprint(data1)

data2 = data1.findAll('dd')
#pprint(data2)

data3 = data2[0].find('span', {'class':'num'}).text
pprint("미세먼지"+data3)
data3 = data2[1].find('span', {'class':'num'}).text
pprint("초미세먼지"+data3)
data3 = data2[2].find('span', {'class':'num'}).text
pprint("오존지수"+data3)