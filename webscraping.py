import requests
res = requests.get("http://www.example.com")
print(type(res))
print(res.text)

import bs4
soup = bs4.BeautifulSoup(res.text,"lxml")
print(soup)
print(soup.select('title'))