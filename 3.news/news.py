from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://media.daum.net/digital/')
#pprint(html.text)

soup = bs(html.text, 'html.parser')
pprint(type(soup))
data1 = soup.find('ul', {'class':'list_mainnews'})
pprint(data1)

#title 가져오기
it_news_list = data1.findAll('a', {'class':'link_txt'})
title_list = [t.text for t in it_news_list]
pprint(title_list);

# href는 어떻게??