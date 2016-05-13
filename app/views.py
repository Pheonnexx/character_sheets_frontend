from app import app
import requests

@app.route('/')
@app.route('/index')
def index():
    response = requests.get('http://0.0.0.0:5002/hello')
    message = response.text
    return message