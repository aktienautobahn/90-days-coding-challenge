import os
from platform import machine

LOGO_COFFEE_MACHINE = """
         C O F F E E      M A C H I N E
        ,adPPYba, 88       88 8b,dPPYba,   
        a8"     "" 88       88 88P'    "8a  
        8b         88       88 88       d8  
        "8a,   ,aa "8a,   ,a88 88b,   ,a8"  
        `"Ybbd8"'  `"YbbdP'Y8 88`YbbdP"'   
                            88           
                            88   
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee = "☕️"
revenue = 0

def update_resources(option):
    #substract ressources by successful transaction
    global resources
    for resource in MENU[option]['ingredients']:
        resources[resource] = resources[resource] - MENU[option]['ingredients'][resource]
    

def process_transaction(option):
    #process
    global revenue       
    
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))*0.25
    dimes = int(input("How many dimes?: "))*0.1
    nickles = int(input("How many nickles?: "))*0.05
    pennies = int(input("How many pennies?: "))*0.01
    amount = round((quarters + dimes + nickles + pennies),2)
    print(f"You have paid ${amount}.")

    
    if amount >= MENU[option]['cost']:
        change = amount - MENU[option]['cost']  
        if change == 0:
            pass
        elif change > 0:
            print(f"Here is ${round(change, 2)} in change.")
            
        print(f"Here ist you {option} {coffee}. Enjoy!")
        update_resources(option)
        revenue += MENU[option]['cost']  
    else:
        print(f"Sorry that's not enough money. Money refunded: ${amount}.")
        

def print_report():
    
    for resource in resources:
        if resource == "water" or resource == "milk":
            print(f"    {resource.capitalize()}: {resources[resource]}ml")
        else:
            print(f"    {resource.capitalize()}: {resources[resource]}g") 
    print(f"    Money: ${revenue}")

def shut_off():
    pass


def greeting():

    return input("What would you like? (espresso/latte/cappuccino): ").lower()
    #ask what the customer wants


def check_resources(option):
    #check if enough water, milk, coffee
    sufficient = []
    for resource in MENU[option]['ingredients']:
        
        if MENU[option]['ingredients'][resource] <= resources[resource]:
            sufficient.append("True")
        else:
            sufficient.append("False")
            
    if "False" in sufficient:
        return False
    else: return "True"

os.system('cls' if os.name == 'nt' else 'clear')
print(LOGO_COFFEE_MACHINE)
machine_on = True
while machine_on:
    option = greeting()
    if option == "off":
        machine_on = False 
    elif option == "report":
        print_report()
    
    elif (check_resources(option)):
        process_transaction(option)
    else:
        print("Option is wrong. Please try again!")
    
