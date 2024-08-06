from json.tool import main
import re
from functools import wraps


# def remove_punctuation(f): # removes punctuation
#     @wraps(f)
#     def wrapper(*args):
#         print("started decorator")
#         print(*args)
#         return re.sub(r'[!?.:;,"()-]', "", *args)
#     return wrapper


MORSE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

# @remove_punctuation
def morse_converter(text):
    text = re.sub(r'[!?.:;,"()-]', "", text) # removes punctuation
    converted_text = ""
    for symbol in text.upper():

        if symbol == ' ':
            converted_text += '       ' # seven spaces between words
        
        else:
            converted_text += MORSE[symbol]
            converted_text += '   ' #three spaces between symbols/letters


    return converted_text




input_text = input('Input your sentence you want to convert into a morse code: ')

output_text = morse_converter(input_text)

print(output_text)