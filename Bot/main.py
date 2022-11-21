from app import keep_alive

from flask import Flask, render_template, request
from waitress import serve
from threading import Thread

from utilities.all_imports import *
from utilities.helpers import *


""" Production server"""
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    keep_alive()
    return render_template("index.html")

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    serve(app, host="0.0.0.0", port=port)



if __name__ == "__main__":
    run_flask()

