'''Print the first 500 characters'''

import requests

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

print(response.text[:500])