#! /bin/env python3

from art import logo, alphabet

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def art():
  print(logo)
  
def cipher(type, message, shift):
  shifted_list = []
  output = []
  if type == "encode":
    for letter in list(message):
      shifted_list = []
      shifted_list = alphabet + alphabet[0:shift]
      output.append(shifted_list[shifted_list.index(letter) + shift])
    string = "".join(map(str,output))
    print(f"The encoded text is {string}\n")
  elif type == "decode":
    for letter in list(message):
      shifted_list = alphabet[0:shift] + alphabet
      output.append(shifted_list[shifted_list.index(letter) - shift])
    string = "".join(map(str,output))
    print(f"The decoded text is {string}\n")
  else:
    print("enter correct command\n")

art()

counter = 0
while True:
  counter +=1 
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  cipher(type = direction, message = text, shift = shift)
  hren = input("Do you wanna start again? Type Y or N: ") 
  if hren == "N":
    break
  elif hren == "Y":
    pass