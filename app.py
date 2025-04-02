from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Mystic Frog Oracle is LIVE!'
