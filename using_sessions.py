# using the default cookie-based (client-side based) sessions in flask
import os
from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)
#app.secret_key = os.urandom(32) # secret key is used to cryptographically sign cookies
app.secret_key = "something".encode()


@app.route('/')
def index():
    if 'username' in session:
        return 'Already logged in as {}'.format(session['username'])
    return 'You are not logged in'
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            session['username'] = username
            return 'Logged in as {}'.format(username)
        return 'Please provide username'
    else:
        if 'username' in session:
            return '{}, you are already logged in'.format(session['username'])
        return '''
               <form action="/login" method="post">
                   Username:<br>
                   <input type="text" name="username">
                   <br><br>
                   <input type="submit" value="Submit">
               </form>
               '''
               
@app.route('/logout')
def logout():
    if session.pop('username', None):
        return 'Successfully logged out'
    return redirect(url_for('index'))