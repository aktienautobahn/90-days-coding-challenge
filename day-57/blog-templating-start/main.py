from flask import Flask, render_template
import json
import os
import sys
from post import Post
from getnews import get_news


COMPANY = 'Tesla'

here = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(here, 'static/news.json')

app = Flask(__name__)


#loading articles as objects into the objects list

dict_articles = get_news(company=COMPANY) 
articles_list = []
num = 0
for article in dict_articles['articles']:


    articles_list.append(
                        Post(
                            id = num,
                            author=article['author'],
                            title=article['title'],
                            description=article['description'],
                            url=article['url'],
                            urlToImage=article['urlToImage'],
                            publishedAt=article['publishedAt'],
                            content=article['content'],
                        ))
    num += 1


@app.route('/')
def home():
    print(articles_list)

    return render_template("index.html", articles=articles_list, topic=COMPANY)


@app.route('/article/<id>')
def get_blog(id):

    return render_template('post.html', article=articles_list[int(id)], topic=COMPANY) 

if __name__ == "__main__":
    app.run(debug=True)
