
from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World, changes!</p>"

print()
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'




