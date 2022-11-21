from flask import *
app = Flask(__name__)
@app.route('/hello')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/login')
def login():
    return "<p>Hello, Login, Its Nice, Good</p>"


@app.route('/home')
def home():
    return render_template('home.html')


app.run(debug=True)
#http://127.0.0.1:5000/hello
#http://127.0.0.1:5000/login