#import bot
from ggl_bot.bot import ggl 

pd = ggl()

#manipulate bot

try:
    pd.gglpop()# remove privacy banner

except:
    pass

pd.searching('AAPL') #search keywords in google

pd.results(20) #search for n pages and save results in a csv
