from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login_page():
    if request.method == 'POST':
        user = request.form['name']
        password = request.form['password']
        return render_template('results.html', name=user, password=password)

if __name__ == '__main__':
    app.run(debug=True)