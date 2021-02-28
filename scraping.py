import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'
res = requests.get(url)

soup = BeautifulSoup(res.text, features="lxml")

# for i, h2_tag in enumerate(soup.find_all('h2')):
#     print(i, h2_tag.text) 
# 
# h2_text_list = []
# 
# for h2_tag in soup.find_all('h2'):
#     h2_text_list.append(h2_tag.text)
# 
# print(h2_text_list)

print(len(soup.find_all('span')))
print(soup.find_all('span', class_='say-no-more'))
print(soup.find_all('span', {'class': 'say-no-more'}))
print(soup.find_all('span', class_=['say-no-more', 'message']))