from art import logo_calc
import os


def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


operation = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide,
}



def calculator():
    print(logo_calc)
    n1 = float(input("What's the first number? "))
    for symbol in operation:
        print(symbol)
    further = True

    while further:
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What's your next number?: "))
        calc_func = operation[operation_symbol]
    
        answer = calc_func(n1, n2)    
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        disicion = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start over, or type 'e' to exit the calculator: ").lower()
        if  disicion == 'y':   
            n1 = answer
        elif disicion == 'n':
            further = False
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()
        elif disicion == 'e':
            further = False

os.system('cls' if os.name == 'nt' else 'clear')
calculator()