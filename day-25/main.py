# import csv

# with open('/Users/emilskorov/Sandbox/python/day-25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:

#     print(data)


import pandas as pd
# from statistics import mean
# weather_data = pd.read_csv('/Users/emilskorov/Sandbox/python/day-25/weather_data.csv')
# #print(type(weather_data))
# temp_list = weather_data['temp'].to_list()
# #print(mean(temp_list))
# #print(sum(temp_list)/len(temp_list))
# monday = weather_data[weather_data['day'] == 'Monday']
# temp_f = (int(monday.temp) * 9/5) + 32
# print(temp_f)


squirrels = pd.read_csv('/Users/emilskorov/Sandbox/python/day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
stats = squirrels['Primary Fur Color'].value_counts()
stats.to_csv('/Users/emilskorov/Sandbox/python/day-25/stats.csv')