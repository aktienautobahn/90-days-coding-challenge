

#TODO 1. Create a dictionary in this format:
import pandas as pd

alphabet = pd.read_csv('./day-26/NATO-alphabet-start/nato_phonetic_alphabet.csv').set_index('letter')

alphabet = alphabet.to_dict()['code']

#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


ask = True
while ask:
    word = input('Enter your name: ').upper()
    result = []
    try:
        result = [alphabet[letter] for letter in word]
    except KeyError:
        print("There is no such key(s) in the NATO Alphabet")
    else:
        ask = False
    
print(result)
