
from calendar import c
from art import logo_hl, vs_hl
from game_data import data
import random
import os
# TODO1:

# TODO2:
os.system('cls' if os.name == 'nt' else 'clear')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
#import random cards
a_choice = random.choice(data)
b_choice = random.choice(data)
if a_choice == b_choice:
    b_choice = random.choice(data)
score = 0
game_stop = False
print(logo_hl)
loop_count = 0


#check answer function
def check_answer_(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


#while loop
while not game_stop:
    #clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo_hl)
    if loop_count > 0:
        #print who wins
        print(f"{bcolors.OKBLUE}You're right! Current score: {score}.{bcolors.ENDC}")
        a_choice = b_choice
        b_choice = random.choice(data)

        if a_choice == b_choice:
            b_choice = random.choice(data)

    #print the choice vs choice
    print(f"Compare A: {a_choice['name']}, a {a_choice['description']}, from {a_choice['country']} ")
    print(f"\n{vs_hl}\n")
    print(f"Compare B: {b_choice['name']}, a {b_choice['description']}, from {b_choice['country']} ")
    #input your choice between two cards: a vs b
    players_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = a_choice['follower_count']
    b_followers = b_choice['follower_count']
    is_correct = check_answer_(players_choice , a_followers, b_followers)

    if is_correct:
        score += 1 
    else:
        game_stop = True
        print(f"{bcolors.WARNING}Sorry, that is wrong. Final score: {score}{bcolors.ENDC}")
    
    loop_count += 1







