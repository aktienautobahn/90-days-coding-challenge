from art import logo_bj
import os
from random import choice

def play():
    os.system('cls' if os.name == 'nt' else 'clear')
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    my_deck_list = []
    dealer_deck_list = []

    def player_wins():
        print("\nPlayer wins 🎊🎉")
        print(f"Your cards: {my_deck_list}, your score: {calculate(my_deck_list)}\nDealers cards {dealer_deck_list} , his score: {calculate(dealer_deck_list)}")

    def player_loose():
        print("\n Player loose 😢") 
        print(f"Your cards: {my_deck_list}, your score: {calculate(my_deck_list)}\nDealers cards {dealer_deck_list} , his score: {calculate(dealer_deck_list)}")


    def take_card():
        rand_index = choice(range(len(cards)))
        card = cards[rand_index]       
        return card

    def calculate(list):
        #calculation result depends on a condition
        if list.count(11):
            summe = sum(list)
            if summe == 21:
                return summe
            elif summe > 21:
                #for each in list.count(11):
                summe -= 10
                return summe
            else:
                return summe

        else: return sum(list)


     
    for _ in range(2): # just loop n-times (range(2))
        my_deck_list.append(take_card()) 
        dealer_deck_list.append(take_card())
    
    print(f"Your cards: {my_deck_list}, current score: {calculate(my_deck_list)}\nDealers first card: {dealer_deck_list[0]}")

    

    while calculate(my_deck_list) < 22: 
        if calculate(my_deck_list) == 21:
            break
        elif input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            my_deck_list.append(take_card())
             
            print(f"Your cards: {my_deck_list}, current score: {calculate(my_deck_list)}\nDealers first card: {dealer_deck_list[0]}")
        
        else: break         

    while calculate(dealer_deck_list) < 17:
        dealer_deck_list.append(take_card())

            
    #my score over 21
    if calculate(my_deck_list) > 21:
        player_loose()
    
    #my score equals 21
    elif calculate(my_deck_list) == 21:
        if calculate(dealer_deck_list) == 21:
            player_loose()
        else:
            player_wins()
    #if both not: then compare with dealers score
    
    elif calculate(my_deck_list) < calculate(dealer_deck_list):
        if calculate(dealer_deck_list) > 21:
            player_wins()
        else:
            player_loose()
    #if scores are equal
    elif calculate(my_deck_list) == calculate(dealer_deck_list):
        print("Draw")
    #else player wins
    else:
            player_wins()
    
   
    if input("\nDo you want to play a game of Balckjack again? Type 'y' or 'n': ") == 'y':
        play()
    else:
        print("Good bye!")
        pass
    


os.system('cls' if os.name == 'nt' else 'clear')
print(logo_bj)
if input("Do you want to play a game of Balckjack? Type 'y' or 'n': ") == 'y':
    play()
else:
    print("Good bye!")