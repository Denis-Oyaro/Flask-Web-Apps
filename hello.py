from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'
    
@app.route('/hello')
def hello():
    return 'Hello, World!'
    
@app.route('/user/<username>')
def show_ser_profile(username):
    return 'User %s' % username
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id
    
@app.route('/path/<path:sub_path>')
def show_path(sub_path):
    return 'Subpath %s' % sub_path
    
@app.route('/projects/')
def projects():
    return 'The projects page'
    
@app.route('/about')
def about():
    return 'The about page'
    
    
