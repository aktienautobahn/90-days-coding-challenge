import os
from random import choice

#players list
players = ['X', 'O']

# game map
cell_map = {
    'x11': ' ',
    'x12': ' ',
    'x13': ' ',
    'x21': ' ',
    'x22': ' ',
    'x23': ' ',
    'x31': ' ',
    'x32': ' ',
    'x33': ' '
    
}

motion = []

#initial values --> empty 


def print_screen(cell_map):
    print('   1    2    3')

    print(f"1 {cell_map['x11']}  |  {cell_map['x12']}  |  {cell_map['x13']}")
    print('  -------------')
    print(f"2 {cell_map['x21']}  |  {cell_map['x22']}  |  {cell_map['x23']}")
    print('  -------------')
    print(f"3 {cell_map['x31']}  |  {cell_map['x32']}  |  {cell_map['x33']}")


def player_input(player):
    global cell_map
    try_again = True
    while try_again:
        print(f"Player {player.upper()}'s turn")
        cell = 'x'+str(input(f"Please choose cell: "))
        try:
            if cell_map[cell] == ' ':
                cell_map[cell] = player.upper()
                try_again = False
            else:
                print('Cell is already filled, try again!')
        except:
            print('Wrong cell, try again')


# check winner's combinations
def winner():
    global cell_map
    if cell_map['x11'] == cell_map['x12'] and cell_map['x11'] == cell_map['x13']:
        if cell_map['x11'] != ' ':
            return cell_map['x11']

    elif cell_map['x21'] == cell_map['x22'] and cell_map['x21'] == cell_map['x23']:
        if cell_map['x21'] != ' ':
            return cell_map['x21']
    
    elif cell_map['x31'] == cell_map['x32'] and cell_map['x31'] == cell_map['x33']:
        if cell_map['x31'] != ' ':
            return cell_map['x31'] 
    
    elif cell_map['x11'] == cell_map['x21'] and cell_map['x11'] == cell_map['x31']:
        if cell_map['x11'] != ' ':
            return cell_map['x11']
    
    elif cell_map['x13'] == cell_map['x23'] and cell_map['x13'] == cell_map['x33']:
        if cell_map['x13'] != ' ':
            return cell_map['x13']
    
    elif cell_map['x11'] == cell_map['x22'] and cell_map['x11'] == cell_map['x33']:
        if cell_map['x11'] != ' ':
            return cell_map['x11']
    
    elif cell_map['x13'] == cell_map['x22'] and cell_map['x13'] == cell_map['x31']:
        if cell_map['x13'] != ' ':
            return cell_map['x13']
    
    elif cell_map['x12'] == cell_map['x22'] and cell_map['x12'] == cell_map['x32']:
        if cell_map['x12'] != ' ':
            return cell_map['x12']
    else:
        return False 


empty_cells = 0
#initial player
player = choice(players)  

game_continue = True


while game_continue:
    os.system('clear') #clear screen

    #switch players
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
    
    #'render' game map
    print_screen(cell_map)
    #Get input
    player_input(player)
        
    
    empty_cells = 0
    for key in cell_map:
        if cell_map[key] == ' ': # if cell is empty
            empty_cells += 1

    if empty_cells == 0:
        os.system('clear') #clear screen
        print_screen(cell_map) 
        print('No winner, it is draw! Goodbye!')   
        game_continue = False

    


    
    #check if no cell is empty



        
    if winner():
        os.system('clear') #clear screen
        print_screen(cell_map) 
        print(f'The winner is {winner()}. Goodbye!')
        game_continue = False
    

    


    
    
