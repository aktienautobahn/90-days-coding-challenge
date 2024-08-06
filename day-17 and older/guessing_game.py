import random
import os
os.system('cls' if os.name == 'nt' else 'clear')
random_num = random.randint(1,100)

def compare_func(num, guess):
    if num == guess: return "Right guess!"
    elif num < guess: return "Too high"
    else: return "Too low"

#while loop for easy & while loop for hard
def play():
    global trial #--> why trial as global but not random_num? 
    further = True

    while further:
        if trial > 0:
            print(f"You have {trial} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if compare_func(random_num, guess) == "Right guess!":
                further = False
                print(compare_func(random_num, guess))
                print("Good Bye!")
                
            else:
                print(compare_func(random_num, guess))

                
            trial -= 1
        else: further = False

level = input("Welcome to the Number Guessing Game!\nChoose a difficulty. Type 'easy' or 'hard':").lower()
print("I am thinking of a number between a number between 1 and 100")
if level == "hard":
    trial = 5
    play()
elif level == "easy":
    trial = 10
    play()
else: print("Wrong entry. Good bye!")