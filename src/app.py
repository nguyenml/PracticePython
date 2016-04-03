from flask import Flask, render_template
import pymongo
from game import Game

import thread

app = Flask(__name__)
mongo = pymongo.MongoClient()
db = mongo['Conway']

@app.route("/")
def hello():
    return render_template("helloworld.html")

@app.route("/test")
def test():
    return render_template("helloworld.html")

if __name__ == "__main__":
    print("Launching web application.")
    # thread.start_new_thread(app.run,())
    print("Launching simulation.")
    #g = Game(db)
    app.run()

