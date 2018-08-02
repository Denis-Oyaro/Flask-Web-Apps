from flask import Flask, flash, render_template

app = Flask(__name__)
app.secret_key = "my_flash_key".encode()

@app.route('/')
def index():
    flash('I love Jesus Christ')
    return '<h1>Flash message set</h1>'
    
@app.route('/flash')
def show_flash():
    return render_template('flash.html')
