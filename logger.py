from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.debug('This is a debug')
    app.logger.warning('This is a warning')
    app.logger.error('This is an error')
    return '<h1>Hola</h1>'