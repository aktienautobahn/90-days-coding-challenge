import os
from urllib import response
from bs4 import BeautifulSoup as bs4
import requests

# here = os.path.dirname(os.path.abspath(__file__))
# html_file =os.path.join(here, 'website.html')


# with open(html_file, "r") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# # all_tags = soup.find_all(name="a")
# #print(soup.title.string)
# #print(soup.prettify())"

# # for tag in all_tags:
# #     #print(tag.getText())
# #     print(tag.get("href"))


# section_heading = soup.find_all(name="h3", class_="heading")
# print(section_heading)

response = requests.get("https://news.ycombinator.com")
yc_news_page = response.text

soup = bs4(yc_news_page, "html.parser")
selection_titles = soup.find_all(name='a', class_='titlelink')
selection_scores = soup.find_all(name='span', class_='score')

titles = [title.getText() for title in selection_titles]
links = [link.get("href") for link in selection_titles]
scores = [int(score.getText().split()[0]) for score in selection_scores ]


# mapped = zip(titles,links,scores)
# for i, (title, link, score) in enumerate(mapped):
#     print(i, score, title, link)

# for ind in range(len(titles)):
#     print(titles[ind])
#     print(links[ind])
#     print(scores[ind])

# print(titles[scores.index(max(scores))])
# print(links[scores.index(max(scores))])

print(len(titles),len(links), len(scores))