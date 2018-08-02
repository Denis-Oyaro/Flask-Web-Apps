from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
def index():
    firstName = request.cookies.get('firstName')
    lastName = request.cookies.get('lastName')
    if firstName and lastName:
        return '<h1>Ciao, {} {}!</h1>'.format(firstName, lastName)
    
    resp = make_response("Hello...")
    resp.set_cookie('firstName', 'Denis')
    resp.set_cookie('lastName', 'Oyaro')
    return resp