import requests
from bs4 import BeautifulSoup

url = 'https://www.tcgplayer.com/product/123456'

r = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(r.text,"html.parser")
print(soup.prettify)