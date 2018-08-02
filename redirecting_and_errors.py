from flask import Flask, request, redirect, abort, url_for, render_template, make_response


app = Flask(__name__)

form = '''
  <form action="/login" method="POST">
  First name:<br>
  <input type="text" name="firstname">
  <br>
  Last name:<br>
  <input type="text" name="lastname">
  <br><br>
  <input type="submit" value="Submit">
</form>
'''

@app.route('/')
def index():
    return redirect(url_for('login'))
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return form
    else:
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        if not first_name or not last_name:
            abort(401) # access denied error code
        return '<h1>Jambo, {} {}!</h1>'.format(first_name, last_name)
        
@app.errorhandler(401)
def access_denied(error):
    resp = make_response(render_template('handle_error.html'), 401)
    resp.headers['content-type'] = 'text/plain'
    return resp
    
        