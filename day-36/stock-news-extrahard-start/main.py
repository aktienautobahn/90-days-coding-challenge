from turtle import end_poly
import pandas_datareader.data as web
import pandas as pd
import requests
from datetime import datetime as dt
import json
import html2text
#from newsapi import NewsApiClient


NEWS_API_KEY = ''

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

time_now = dt.now()
today = time_now.day
month = time_now.month
year = time_now.year
end = dt(year,month,today-1)
start = dt(year,month,today-2) 
df = web.DataReader("TSLA", data_source='yahoo', start=start, end=end)
df.Close = df.Close.pct_change(periods = 1)

if abs(df.Close[1]) > 0.05: #average volatility based ? 
    print("Get News on TSLA")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
# /v2/top-headlines
    parameters = {
                    "q":COMPANY_NAME,
                    "from":f"{year}-{month}-{today-1}",
                    "sortBy":"popularity",
                    "apiKey": NEWS_API_KEY
                }

    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    news_data = response.json()["articles"]
    articles = news_data[:3]

    #print(json.dumps(news_data, sort_keys=True, indent=4))

    # top_news_title = [news["title"] for news in news_data[:3]]
    # top_news_description = [html2text.html2text(news["description"]) for news in news_data[:3]]
    # top_news = {title:description for (title,description) in zip(top_news_title,top_news_description)}
    #print(top_news_description)

    

sms_text = [f"Headline: {article['title']}\nBrief:{html2text.html2text(article['description'])}" for article in articles] 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
if df.Close[1] < -0.05:
    for text in sms_text:
        top_articles = f"{STOCK} 🔻{round(df.Close[1]*100, 2)}%\n{text}"


elif df.Close[1] > 0.05:
    for news in sms_text:
        top_articles = f"{STOCK} ⬆{round(df.Close[1]*100, 2)}%\n{text}"


print(top_articles)
        #here send sms function

    
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

