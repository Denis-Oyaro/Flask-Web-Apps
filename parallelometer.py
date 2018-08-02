from flask import Flask, request, make_response
import requests
import threading
import time
import random

app = Flask(__name__)


# HTML main page. This page has 16 iframes, each of which causes
# the browser to send an additional request to this server.
# Each iframe will display the number of currently active requests.
html = '''<!DOCTYPE html>
<title>Things!</title>
<style>iframe { width: 23%; border: 0 }</style>
<iframe src="/frame/0"></iframe> <iframe src="/frame/1"></iframe>
<iframe src="/frame/2"></iframe> <iframe src="/frame/3"></iframe>
<iframe src="/frame/4"></iframe> <iframe src="/frame/5"></iframe>
<iframe src="/frame/6"></iframe> <iframe src="/frame/7"></iframe>
<iframe src="/frame/8"></iframe> <iframe src="/frame/9"></iframe>
<iframe src="/frame/a"></iframe> <iframe src="/frame/b"></iframe>
<iframe src="/frame/c"></iframe> <iframe src="/frame/d"></iframe>
<iframe src="/frame/e"></iframe> <iframe src="/frame/f"></iframe>
'''

# Track the number of requests that are in progress.
# This variable will get +1 every time a handler starts processing
# a request, and -1 every time it finishes.
inflight = 0

# To protect the inflight variable from being changed from multiple
# request handlers at once, we need to use a lock.
lock = threading.Lock()

@app.route('/')
@app.route('/frame/<num>')
def show_frames(num=None):
    global inflight, lock
    with lock:
        # We're starting to handle a request.
        inflight += 1
    if request.path.startswith('/frame'):
        # This request is for iframe contents.
        time.sleep(random.random())  # Slow down by 0-1 seconds.
        resp = make_response('{} requests in flight'.format(inflight))
    else:
        # This request is for the main page.
        resp = make_response(html)
    with lock:
        # We're done handling a request.
        inflight -= 1
    return resp
    
# if __name__ == '__main__':
    # app.debug=True
    # app.run('0.0.0.0', 5000, threaded=False)
