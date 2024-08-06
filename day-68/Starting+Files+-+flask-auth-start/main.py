from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_session import Session
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
# from wtforms.validators import DataRequired
# from wtforms.fields import StringField, PasswordField, SubmitField
# from wtforms.fields.html5 import EmailField


app = Flask(__name__)



app.config['SECRET_KEY'] = 'any-complicated-secret-key-you-choose'
# app.config["SESSION_TYPE"] = "filesystem"
# app.config["SESSION_PERMANENT"] = False
app.config['DOWNLOAD_FOLDER'] = "static/files"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Session(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB.
# db.delete_all() 
#db.create_all()

# class RegisterForm(FlaskForm):
#     username = StringField("username", validators=[DataRequired()])
#     email = EmailField("e-mail", validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     submit = SubmitField()

# class LoginForm(FlaskForm):
#     username = StringField("username", validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     submit = SubmitField()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods = ["GET", "POST"])
def register():

    if request.method == "POST":
        add_user = User()

        for arg, value in request.form.items():
            if arg in User.__table__.columns:
                setattr(add_user, arg, value)

        if not User.query.filter_by(email=add_user.email).first():
        # session['name'] = add_user.name
            add_user.password = generate_password_hash(request.form.get("password"), 
                                                        method="pbkdf2:sha256", 
                                                        salt_length=8)
            print(session)
            db.session.add(add_user)
            db.session.commit()
                    #Log in and authenticate user after adding details to database.
            login_user(add_user)
            return redirect(url_for('secrets'))
        else:
            flash("User already exists")
            return redirect("login")

    return render_template("register.html")


@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = User()

        for arg, value in request.form.items():
            if arg in User.__table__.columns:
                setattr(user, arg, value)


        if User.query.filter_by(email=user.email).first():
            user_found = User.query.filter_by(email=user.email).first()
            # print('user_found = True')
            if check_password_hash(user_found.password, user.password):
                # print('password verified')
                # print(user_found.name)
                # session['name'] = user_found.name
                login_user(user_found)
                return redirect(url_for("secrets"))
            else:
                # print('password unverified')
                flash("Invalid password")
                return render_template("login.html")
        else:
            print('user not found')
            flash("User not found")
            return render_template("login.html")

    return render_template("login.html")


@app.route('/secrets/', methods = ["GET"])
@login_required
def secrets():
    # print(session.get("name"))
    # if not session.get("name"):
    #     print('redirect login')
    #     return redirect("/login")
    # name = request.args.get("name")

    return render_template("secrets.html")#, name=session.get("name"))


@app.route('/logout')
def logout():
    # session["name"] = None
    logout_user()
    return redirect("/")


@app.route('/download/<path:filename>')
@login_required
def download(filename):
    print(filename)
    print(app.config['DOWNLOAD_FOLDER'])
    return send_from_directory(
        app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True
    )



if __name__ == "__main__":
    app.run(debug=True)
