from app import app
import requests

cs_api_route='http://0.0.0.0:5002'


@app.route('/')
@app.route('/index')
def index():
    response = requests.get('{}/hello'.format(cs_api_route))
    message = response.text
    return message


@app.route('/getcharacter/<name>', methods=['GET'])
def get_character(name):
    response = requests.get('{}/character/{}'.format(cs_api_route, name))
    message = response.text
    return message
