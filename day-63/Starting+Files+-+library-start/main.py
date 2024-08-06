from enum import unique
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy import null
# ---------------------------- SET FILE PATH --------------------------- # 
basedir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'books-collection.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Title('{self.title}')"


all_books = []

@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=("GET","POST"))
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        add_book = Books(title=title, author=author, rating=rating)
        db.session.add(add_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit", methods=("GET","POST"))
def edit():
    if request.method == 'POST':
        book_id = request.args.get('id')
        rating = request.form['rating']
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = rating 
        db.session.commit()  
        return redirect(url_for('home'))
    
    else:
        book_id = request.args.get('id')
        book_to_update = Books.query.get(book_id)
        return render_template('edit.html', book = book_to_update )

@app.route("/delete", methods=['GET','POST'])
def delete():
    id = request.args.get('id')

    book_to_delete = Books.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

