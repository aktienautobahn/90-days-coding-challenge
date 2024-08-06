from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/guess/<name>')
def guess(name):
    age = requests.get('https://api.agify.io?name='+name).json()['age']
    gender = requests.get('https://api.genderize.io?name='+name).json()['gender']
    return render_template('guess.html', name=name, age=age, gender=gender)



if __name__ == '__main__':
    app.run(debug=True)