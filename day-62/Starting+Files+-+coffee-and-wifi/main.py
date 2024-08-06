from flask_wtf.csrf import CSRFProtect
import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL, ValidationError
import csv

# ---------------------------- SET FILE PATH --------------------------- # 
here = os.path.dirname(os.path.abspath(__file__))


# ---------------------------- API URL --------------------------- # 
URL = 'https://cafes-app.herokuapp.com'



app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = ''
app.config['SECRET_KEY'] = ''
Bootstrap(app)

def _url_required(form, field):
    if not field.raw_data[:5] == 'https':
        raise ValidationError('URL invalid')

class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)',   validators=[DataRequired(), _url_required])
    open = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()]) 
    close = StringField(label='Closing Time e.g. 5:30PM', validators=[DataRequired()]) 
    rating = SelectField(label='Cafe Rating', choices=['☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕'], validators=[DataRequired()]) 
    wifi = SelectField(label='WiFi Strength Rating', choices=['✘','💪','💪💪','💪💪💪'], validators=[DataRequired()]) 
    power = SelectField(label='Power Sockets',choices=['✘','🔌','🔌🔌','🔌🔌🔌'], validators=[DataRequired()]) 
    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CafeForm()
    if form.validate_on_submit():

        newRow = ','.join((form.cafe.data, 
                            form.location.data, 
                            form.open.data,
                            form.close.data,
                            form.rating.data,
                            form.wifi.data,
                            form.power.data))

        with open(os.path.join(here, 'cafe-data.csv'), "a") as f:
            f.write('\n' + newRow)
        return redirect(url_for('cafes'))
    else:
        print(form.cafe.errors)
        print(form.location.errors)
        print(form.open.errors)
        print(form.close.errors)
        print(form.rating.errors)
        print(form.wifi.errors)
        print(form.power.errors)
        print('Fehler')
        


    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():

    with open(os.path.join(here, 'cafe-data.csv'), newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            
    response = requests.get(
                            url=URL+'/all'
    )
    
    cafes = response.json()['cafes']
    for cafe in cafes:
        print(cafe)
    
    

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
