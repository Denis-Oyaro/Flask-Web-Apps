from flask import Flask, request, url_for
import requests

app = Flask(__name__)

form = '''<form action="/login" method="POST">
  First name:<br>
  <input type="text" name="firstname">
  <br>
  Last name:<br>
  <input type="text" name="lastname">
  <br><br>
  <input type="submit" value="Submit">
</form>'''


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return form
    else:
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        return 'Welcome, %s %s' % (firstname, lastname)
        
@app.route('/answer')
def get_answer():
    return 'Here is the answer'
    
    
@app.route('/request')
def make_request():
    r = requests.get('http://localhost:5000/answer')
    if r.status_code != 200:
        return 'NOT GOOD'
    return r.text
    