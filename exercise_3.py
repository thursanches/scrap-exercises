from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

quotes = soup.find_all('div', class_='quote')

all_authors = set()
for quote in quotes:
  text = quote.find('span', class_='text')
  print(text.get_text(strip=True))
  author = quote.find('small', class_='author')
  print(author.get_text(strip=True))

  all_authors.add(author)

print(f"A quantidade de frases é de {len(quotes)}")
print(f'Quantidade única de autores: {len(all_authors)}')