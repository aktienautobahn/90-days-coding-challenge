from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):

    login = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

app = Flask(__name__)
Bootstrap(app)
# Flask-WTF requires an encryption key - the string can be anything
csrf = CSRFProtect(app)
app.secret_key = 'put your api secret key here'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.login.data == 'put your email here' and \
            login_form.password.data == 'put your password here':
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)

@app.route('/success')
def success():
    return '<center><h1>You submitted successfully</h1></center>'

if __name__ == '__main__':
    app.run(debug=True)