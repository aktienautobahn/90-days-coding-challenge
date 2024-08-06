import re

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

# morse converter function
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

        

#get text from user
input_text = input('Input your sentence you want to convert into a morse code: ')

#convert text and assign to a variable as a string
output_text = morse_converter(input_text)

#print out the variable
print(output_text)