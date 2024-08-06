#TODO: 
# 
#creating names list from the read file
invited_names = open('./Input/Names/invited_names.txt')
letter = open('./Input/Letters/starting_letter.txt')
name_list =[]
for name in invited_names.readlines():
    name_list.append(name.replace("\n", ""))

invited_names.close()

# Create a letter using starting_letter.txt 
for name in name_list:
    letter_lines = letter.readlines()
    letter_lines[0] = letter_lines[0].replace("[name]", name)
    with open("./Output/"+name) as letter_ready:
        letter_ready.write()
temp_letter = []
for name in name_list:
    temp_letter.clear()
    print(letter_lines)
    print(temp_letter)
    temp_letter = letter.readlines()
    temp_letter[0] = temp_letter[0].replace("[name]", name)
    print(temp_letter)
    
#letter.close()
        




#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
