from newsapi import NewsApiClient
import json
from config import news_api_key


newsapi = NewsApiClient(news_api_key)

def get_news(company):
    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q=company,
                                            
                                            #sources='bbc-news,the-verge',
                                            category='business',
                                            language='en',
                                            country='us',
                                            page_size=10)
    return top_headlines

    # # /v2/everything
    # all_articles = newsapi.get_everything(q='bitcoin',
    #                                       sources='bbc-news,the-verge',
    #                                       domains='bbc.co.uk,techcrunch.com',
    #                                       from_param='2017-12-01',
    #                                       to='2017-12-12',
    #                                       language='en',
    #                                       sort_by='relevancy',
    #                                       page=2)

    # # /v2/top-headlines/sources
    # sources = newsapi.get_sources()
    # with open('static/news.json', 'w') as file:
    #     json.dump(top_headlines, file)