from flask_wtf.csrf import CSRFProtect
import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL, ValidationError
import csv

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'cafes.db')


db = SQLAlchemy()

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = ''
app.config['SECRET_KEY'] = ''
Bootstrap(app)

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{db_path}'
# initialize the app with the extension
db.init_app(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.String(10), nullable=False)
    has_toilet = db.Column(db.String(10), nullable=False)
    has_wifi = db.Column(db.String(10), nullable=False)
    can_take_calls = db.Column(db.String(10), nullable=False)
    seats = db.Column(db.String(250))
    coffee_price = db.Column(db.String(250))





class CafeForm(FlaskForm):
    name = StringField(label='Cafe Name', validators=[DataRequired()])
    map_url = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    img_url = StringField(label='Image URL', validators=[DataRequired(), URL()])
    location = StringField(label='Location', validators=[DataRequired()])
    has_sockets = SelectField(label='Power Sockets',choices=['✘','🔌','🔌🔌','🔌🔌🔌'], validators=[DataRequired()]) 
    has_toilet = SelectField(label='Has Toilet', choices=['yes', 'no'],validators=[DataRequired()])
    has_wifi = SelectField(label='WiFi Strength Rating', choices=['✘','💪','💪💪','💪💪💪'], validators=[DataRequired()]) 
    can_take_calls = SelectField(label='Can Take Calls',choices=['yes', 'no'], validators=[DataRequired()])
    seats = StringField(label='Number of Seats',validators=[DataRequired()])
    coffee_price = SelectField(label='Coffee Price',choices=['$','$$', '$$$'],validators=[DataRequired()])
    submit = SubmitField(label='Submit')




# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CafeForm()
    if form.validate_on_submit():
    # Create new Cafe object
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )
        # Add the new cafe to the session
        db.session.add(new_cafe)
        # Commit the session to save the changes in the database
        db.session.commit()

        # Redirect to the cafes page after successful addition
        return redirect(url_for('cafes'))





@app.route('/cafes')
def cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
    return render_template('cafes.html', cafes=all_cafes)


if __name__ == '__main__':
    app.run(debug=True)
