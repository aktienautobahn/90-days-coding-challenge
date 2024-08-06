from turtle import title
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from redis import AuthenticationError
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime 




app = Flask(__name__)
app.config['SECRET_KEY'] = ''
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)

Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    requested_post = BlogPost.query.get(index)
    # for blog_post in posts:
    #     if blog_post["id"] == index:
    #         requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods = ["GET","POST"])
def make_post():
    form = CreatePostForm()
    if request.method == "POST":
        title = form.title.data
        subtitle = form.subtitle.data
        date = datetime.now().strftime("%B %d, %Y")
        body = form.body.data
        author = form.author.data
        img_url = form.img_url.data
        new_post = BlogPost(title=title,
                            subtitle=subtitle,
                            date=date,
                            body=body,
                            author=author,
                            img_url = img_url
                            )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form = form)



@app.route("/edit_post/<int:post_id>", methods = ["GET", "POST"])
def edit_post(post_id):
    requested_post = BlogPost.query.get(post_id)


    form = CreatePostForm(
            title = requested_post.title,
            subtitle = requested_post.subtitle,
            author = requested_post.author,
            img_url = requested_post.img_url,
            body = requested_post.body
        )
    if request.method == "POST":
        requested_post.title = form.title.data
        requested_post.subtitle = form.subtitle.data 
        requested_post.body = form.body.data
        requested_post.author = form.author.data
        requested_post.img_url = form.img_url.data

        db.session.commit()

        return redirect(url_for("show_post", index=requested_post.id)) 


    return render_template("make-post.html", form=form)

@app.route('/delete-post/<int:post_id>')
def delete_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    if requested_post:
        print(post_id)
        print(type(post_id))
        db.session.delete(requested_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)