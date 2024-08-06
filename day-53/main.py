import requests
from bs4 import BeautifulSoup

# https://forms.gle/wL6uJXEEVppMhZsp8

macos = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'

headers = {
    'User-Agent': macos,
    'Accept-Language':'en-US,en;q=0.9'   
}
zillow_url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55950011206055%2C%22east%22%3A-122.30715788793945%2C%22south%22%3A37.62031346674776%2C%22north%22%3A37.92994524764116%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

zillow = requests.get(zillow_url, headers=headers, timeout=10)
zillow.raise_for_status()

soup = BeautifulSoup(zillow.text, "html.parser")

# links_names = soup.find_all(name='a', class_='list-card-link')
prices = soup.find_all(name='div', class_='list-card-price')

prices_list = [price.get_text() for price in prices]
print(prices_list)