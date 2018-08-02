from flask import Flask, request

app = Flask(__name__)

form = '''<form action="/login" method="GET">
  First name:<br>
  <input type="text" name="firstname">
  <br>
  Last name:<br>
  <input type="text" name="lastname">
  <br><br>
  <input type="submit" value="Submit">
</form>'''


@app.route('/form')
def show_form():
    return form
    
@app.route('/login')
def login():
    firstname = request.args.get('firstname', '')
    lastname = request.args.get('lastname', '')
    return 'Welcome, %s %s' % (firstname, lastname)
