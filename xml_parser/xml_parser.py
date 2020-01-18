import bs4 as bs
from urllib.request import Request, urlopen

req = Request('https://medium.com/feed/@sama.shoummo', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup=bs.BeautifulSoup(webpage,'xml')

for item in soup.find_all('title'):
	print(item.text)

print(soup)