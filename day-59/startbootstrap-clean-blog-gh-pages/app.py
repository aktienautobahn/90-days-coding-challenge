from flask import Flask, render_template, request
from post import Post
import requests
import smtplib

app = Flask(__name__)

MY_EMAIL = ""
MY_PASSWORD = ""

endpoint = "https://api.npoint.io/"
response = requests.get(endpoint)
data = response.json()
articles_list = []
for item in data:
    articles_list.append(
                    Post(
                        id = int(item['id']),
                        title=item['title'],
                        subtitle=item['subtitle'],
                        body = item['body']
                    ))


@app.route('/')
def home():

    return render_template('index.html', data=articles_list)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:New Message\n\n{name}\n{email}\n{phone}\n{message}"
    )
    
        return render_template('contact.html', successful = True)

    if request.method == "GET":
        return render_template('contact.html')


@app.route('/post/<id>')
def post(id):
    for article in articles_list:
        if article.id == int(id):
            selected_article = article


    return render_template('post.html', article=selected_article)





if __name__ == "__main__":
    app.run(debug=True)