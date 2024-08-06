from unicodedata import decimal
from bs4 import BeautifulSoup
import requests
from decimal import Decimal


URL = 'https://www.amazon.de/'
#windows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
macos = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'

headers = {
    'User-Agent': macos,
    'Accept-Language':'en-US,en;q=0.9'
    
}


response = requests.get(URL, headers=headers, timeout=10)
print(response)


soup = BeautifulSoup(response.text, 'lxml')

title = soup.find_all(name='span', id='productTitle')[0].getText().strip()
price_whole =  soup.find_all(name='span', class_='a-price-whole')
price_fraction =  soup.find_all(name='span', class_='a-price-fraction')
price_whole = price_whole[0].getText().split(',')[0]

price_fraction = price_fraction[0].getText().strip()
price = Decimal(price_whole + '.' + price_fraction)

print(title)
print(type(price))