import shelve

import settings

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def show_twitter_stats():
    storage = shelve.open('twitter_stats', writeback=True)

    return render_template('index.html', storage=storage)

if __name__ == '__main__':
    app.debug = settings.debug
    app.run(host=settings.server_ip, port=settings.server_port)
