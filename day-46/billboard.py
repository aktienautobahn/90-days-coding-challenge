import requests
from bs4 import BeautifulSoup

URL = 'https://www.billboard.com/charts/hot-100'


class GetBillboardSongs:
    def __init__(self, date) -> None:
        self.get_top_100_page(date=date)
    
    def get_top_100_page(self, date):
        response = requests.get(URL+'/'+date)
        soup = BeautifulSoup(response.text, 'lxml')
        self.parsing(soup)

    def parsing(self, soup):
        titles_list = soup.find_all('h3', class_='a-no-trucate')
        # titles_list = soup.selector('h3.title-of-a-story')
        # print(titles_list)
        musicians_list = soup.find_all(name = 'span', class_='a-no-trucate')
        songs = [title.getText().strip() for title in titles_list]
        musicians = [musician.getText().strip() for musician in musicians_list]
        self.results = dict(zip(songs, musicians))
        return self.results



        




