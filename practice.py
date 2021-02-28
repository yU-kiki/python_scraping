import requests
from bs4 import BeautifulSoup

url = 'https://tech-diary.net/python-scraping-books/'
res = requests.get(url)

soup = BeautifulSoup(res.text, features="lxml")

# h2_and_h3_text_list = []

# for h2_and_h3_tag in soup.find_all(['h2', 'h3']):
#    h2_and_h3_text_list.append(h2_and_h3_tag.text)

h2_and_h3_text_list = [tag.text for tag in soup.find_all(['h2', 'h3'])]

# h2_and_h3_text_list = list(map(lambda s: s.test, soup.find_all(['h2', 'h3'])))

body = soup.find('article')

# print(body.find_all(['h2', 'h3']))

# print(soup.find('article').find_all(['h2', 'h3']))

print(len(soup.find_all(['h2', 'h3'])))

soup.find('h2', {'class': 'post-list-title'}).extract()

print(len(soup.find_all(['h2', 'h3'])))

print(soup.find_all(['h2', 'h3']))