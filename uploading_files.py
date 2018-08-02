from flask import request, Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)

form = '''
<form action="/file" method="post" enctype="multipart/form-data">
  Select a file:<br>
  <input type="file" name="thefile"><br><br>
  <input type="submit" value="Submit">
</form>
'''

@app.route('/file', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return form
    else:
        f = request.files.get('thefile')
        if f:
            f.save('/vagrant/' + secure_filename(f.filename))
        return 'File saved!'
