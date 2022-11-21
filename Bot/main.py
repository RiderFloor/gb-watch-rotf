


from app import star

from flask import Flask, render_template, request
from waitress import serve
from threading import Thread

from utilities.all_imports import *
from utilities.helpers import *


""" Production server"""
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
@app.route("/home")
def home():
	if request.method == 'POST':
		print('force shut down')

	if request.method == 'GET':
		return render_template("index.html")

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    serve(app, host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    s = Thread(target=star)
    t.start()
    wait(10)
    s.start()

if __name__ == "__main__":
    keep_alive()

