from flask import Flask, request
from waitress import serve
from threading import Thread

from app import start_bot

import os, time


""" Production server"""
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		mess = request.json
		start_bot(mess)
		return mess

	if request.metho == 'GET':
		return 'hello world'

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    serve(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
	run_flask()

