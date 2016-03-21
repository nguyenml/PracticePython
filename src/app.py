from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

from game import Game

import thread

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/")
def hello():
    return render_template("helloworld.html")

@app.route("/test")
def test():
    return render_template("helloworld.html")

if __name__ == "__main__":
    print("Launching web application.")
    thread.start_new_thread(app.run,())
    print("Launching simulation.")
    g = Game(mongo)
