#from replit import clear
#from art import logo
#HINT: You can call clear() to clear the output in the console.
#print(logo)
print("")
biders_list = []

def new_bidder():
  name = input("Input your name: ")
  bid = int(input("Input your bid: "))
  biders_list.append({name:bid})
  return biders_list


def find_winner(biders_list):
  values_list = []
  for element in biders_list:
    for value in element:
      values_list.append(element[value])

  print(values_list)  
  max_value = max(values_list)
  print(max_value)
  #function to convert list into a dictionary

  #function to get key from value  
  def get_key(max_value):
    for element in biders_list:
      
      if list(element.values())[0] == max_value:
        return list(element.keys())[0]
      else:
          pass#key_e = element.keys()

      
      #for key, value in element:
      #  print(key)
      #  if value == max_value:
      #    return key
    
  print(f" The winner is {get_key(max_value)} and he bid {max_value}.")
    
  



new_bidder()

while input("Do you have more biders? Y/N: ").lower() == "y":
#  clear()
  new_bidder()
find_winner(biders_list)