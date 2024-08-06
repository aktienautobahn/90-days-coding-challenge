fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
  try:
    fruit = fruits[index]

  except IndexError:
    print("There are only 3 types of pies! Try 0 to 2")
  else:
    print(fruit + " pie")
    
make_pie(2)