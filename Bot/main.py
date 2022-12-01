from flask import Flask, request
from waitress import serve
from threading import Thread

from app import keep_alive

import os, time


""" Production server"""
app = Flask(__name__)
@app.route('/')
def home():
	keep_alive()
	return 'hello world'
def run_flask():
	port = int(os.environ.get('PORT', 5000))
	serve(app, host="0.0.0.0", port=port)



if __name__ == "__main__":
	run_flask()

