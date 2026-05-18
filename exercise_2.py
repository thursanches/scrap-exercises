'''Show the sentences with rescpective author name'''

from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
  text = quote.find('span', class_='text')
  print(text.get_text(strip=True))
  author = quote.find('small', class_='author')
  print(author.get_text(strip=True))