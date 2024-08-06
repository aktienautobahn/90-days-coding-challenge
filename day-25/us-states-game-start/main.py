import pandas as pd
import turtle
from turtle import Screen, Turtle

FONT = ("Courier", 12, "normal")
ALIGNMENT = 'center'

states_df = pd.read_csv('/Users/emilskorov/Sandbox/python/day-25/us-states-game-start/50_states.csv')
all_states = states_df.state.to_list()

screen = Screen()
screen.title('U.S. States Game')
image = '/Users/emilskorov/Sandbox/python/day-25/us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


def get_coordinates(name):
    '''
    get coordinates from either dict states or the states_df Dataframe
    '''

    choicen_state = states_df[states_df.state == name]
    state_name = choicen_state.state

    x_cor = choicen_state.x

    y_cor = choicen_state.y
    print(state_name, x_cor, y_cor)
    return state_name, x_cor, y_cor

def put_state_name(state_name, x_cor, y_cor):
    '''
    write the name of the states with coordinates
    ''' 
    label = Turtle()
    label.hideturtle()
    label.penup()
    label.goto(int(x_cor), int(y_cor))
    label.write(state_name.values[0], font=FONT)


#TODO implement 
counter = 0
print(all_states)

guessed_states = []
while len(guessed_states) < 51:
    answer = screen.textinput(title=f'{counter}/50 states correct', prompt='What is the next state?').title()
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv('/Users/emilskorov/Sandbox/python/day-25/us-states-game-start/missing_states.csv')

        break
    
    try:
        state_name, x_cor, y_cor = get_coordinates(answer)
        put_state_name(state_name, x_cor, y_cor)
        guessed_states.append(answer)
        counter += 1
    except:
        print("there is no that state name")
        pass
    print(guessed_states)

list_to_save = pd.Series(guessed_states)
list_to_save.to_csv('/Users/emilskorov/Sandbox/python/day-25/us-states-game-start/guessed_list.csv')
