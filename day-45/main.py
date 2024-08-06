import requests
from bs4 import BeautifulSoup
import os

here = os.path.dirname(os.path.abspath(__file__))
results =os.path.join(here, 'movies.txt')


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)

movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")

selection_titles = soup.find_all(name='h3', class_='title')



titles_list = [title.getText().split(")") for title in selection_titles]

with open(results, "a") as file:

    for title in reversed(titles_list):
        try:
            file.write(f"{int(title[0])}) {title[1].strip()}\n")
        except ValueError:

            file.write(f"{int(title[0].split(':')[0])}) {title[0].split(':')[1].strip()}\n")



