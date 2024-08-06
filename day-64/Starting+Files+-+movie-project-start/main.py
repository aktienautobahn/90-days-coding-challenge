
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

# ---------------------------- MOVIE API ----------------------------#
MOVIE_API_KEY = ''
TMDB_IMG_URL_PATH = 'https://image.tmdb.org/t/p/w500'
def movies_search_func(movie_title):
    params = {
        'api_key': MOVIE_API_KEY,
        'query':movie_title
        }
    try:
        response = requests.get('https://api.themoviedb.org/3/search/movie', timeout=5, params=params)
        response.raise_for_status()
        # Code here will only run if the request is successful
        movie = response.json()['results']
        return movie
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)


# ---------------------------- SET FILE PATH --------------------------- # 
basedir = os.path.dirname(os.path.abspath(__file__))

# ---------------------------- SET UP APP --------------------------- # 

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
csrf = CSRFProtect(app)
Bootstrap(app)

# ---------------------------- SET UP DATABASE --------------------------- # 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'movies.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), nullable = False, unique = True)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(1000), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    ranking = db.Column(db.Integer, nullable = False)
    review = db.Column(db.String(250), nullable = False)
    img_url = db.Column(db.String(1000), nullable = False)

class MovieSearchForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Search Movie')

class MovieEditForm(FlaskForm):
    ranking = StringField(label='Your Ranking out of 10, e.g.7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Update Movie')

class TMDB:
    def __init__(self, tmdb_id, title, year = 0, description = '', rating ='', img_url=''):
        self.tmdb_id = tmdb_id
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = 0
        self.review = ""
        self.img_url = img_url


def initialize_db():
    db.drop_all()
    db.create_all()
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
            )

    db.session.add(new_movie)
    db.session.commit()
#initialize_db()

@app.route("/")
def home():
    #This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.ranking).all()
    
    #This line loops through all the movies
    for i in range(len(all_movies)):
        #This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies = all_movies)

@app.route('/search', methods=("GET","POST"))
def search():
    global movies_results_list
    if request.method == 'POST':

        search_title = request.form['searchTitle']
        movies = movies_search_func(search_title)


        movies_results_list = []
        for movie in movies:
            try:
                year = int(movie['release_date'][:4] if not movie['release_date'] == '' else 0)
            except:
                movie['release_date'] = 0
            finally:

                movies_results_list.append(TMDB(
                    tmdb_id= movie['id'],
                    title= movie['title'],
                    year = year,
                    description= movie['overview'],
                rating= movie['vote_average'],
                img_url= (movie['poster_path'] if not movie['poster_path'] == None else ""),
                ))
        return render_template('add.html', movies=movies_results_list)

    return render_template('search.html')

@app.route('/add', methods=("GET","POST"))
def add():
    if request.method == "POST":
        movie_to_add_id = int(request.form['result'])
        for movie in movies_results_list:
            if movie.tmdb_id == movie_to_add_id:
                new_movie = Movie(
                    title=movie.title,
                    year=movie.year,
                    description=movie.description,
                    rating=movie.rating,
                    ranking=0,
                    review="",
                    img_url=TMDB_IMG_URL_PATH + movie.img_url,
                        )
                db.session.add(new_movie)
                db.session.commit()
        return redirect(url_for('home'))
        





@app.route('/edit', methods=("GET","POST"))
def edit():
    form = MovieEditForm()
    if request.method == 'POST' and form.validate_on_submit:
        movie_id = request.args.get('id')
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.ranking = form.ranking.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    movie_id = request.args.get('id')


    return render_template('edit.html', movie_id = movie_id, form = form)

@app.route('/delete', methods=("GET","POST"))
def delete():
    id = request.args.get('id')
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
