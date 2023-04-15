import time

from flask import Flask

app = Flask(__name__)


@app.route("/ping")
def pong():
    time.sleep(20)
    return "pong"
