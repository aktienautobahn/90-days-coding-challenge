import random
from flask import Flask
from random import randint

app = Flask(__name__)
random_num = randint(0,9)

@app.route('/')
def home():

    return '<center><h1>Guess a number between 0 and 9</h1></center>'\
            '<center><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></center>'

@app.route('/<int:num>')
def check_if_true(num):
    if num < 0 or num > 9:
        return '<center><h1>Your number must be between 0 and 9, try again!</h1></center>'\
        '<center><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></center>'         
    if num == random_num:
        return '<center><h1>You found me!</h1></center>'\
        '<center><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></center>' 
    elif num > random_num:
        return '<center><h1>To high, try again!</h1></center>'\
        '<center><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></center>' 
    elif num < random_num:
        return '<center><h1>Too low, try again!</h1></center>'\
        '<center><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></center>' 

if __name__ == '__main__':
    app.run(debug=True)