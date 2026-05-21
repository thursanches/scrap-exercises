import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

quotes = soup.find_all('div', class_='quote')

all_authors = set()

for quote in quotes:
  text = quote.find('span', class_='text').get_text(strip=True)
  author = quote.find('small', class_='author').get_text(strip=True)
  all_authors.add(author)
  r_tag = quote.find_all('a', class_='tag')
  tags = []
  for t in r_tag:
    tags.append(t.get_text(strip=True))
  print(text)
  print(author)
  print(tags)
  print('---')