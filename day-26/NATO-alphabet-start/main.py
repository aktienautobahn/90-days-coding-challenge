# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas as pd
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
import pandas as pd

alphabet = pd.read_csv('/Users/emilskorov/Sandbox/python/day-26/NATO-alphabet-start/nato_phonetic_alphabet.csv').set_index('letter')

alphabet = alphabet.to_dict()['code']
print(alphabet)

#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter your name: ').upper()
result = []
# for letter in word:
#     result.append(alphabet[letter])

result = [alphabet[letter] for letter in word]

print(result)
