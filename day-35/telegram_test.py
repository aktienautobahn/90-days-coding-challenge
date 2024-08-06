import requests

response = requests.get(url="placeholder")
response.raise_for_status()

data = response.json()
chat_id = data["result"][0]["message"]["chat"]["id"]

def telegram_bot_sendtext(bot_message):

   bot_token = 'placeholder'
   bot_chatID = str(chat_id)
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)
