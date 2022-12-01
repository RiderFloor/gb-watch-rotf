from flask import Flask, request
from waitress import serve
from threading import Thread

from app import build

import os, time


""" Production server"""
app = Flask(__name__)
@app.route('/')
def home():
	global mess

	if request.json:
		mess = request.json
		return mess
	else:
		return 'hello world'

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    serve(app, host="0.0.0.0", port=port)

def run_bot():
	build(mess)

def keep_alive():
	print('staring thread')
	s = Thread(target=run_flask)
	t = Thread(target=run_bot)
	s.start()
	time.sleep(10)
	t.start()
	print('thread started')


if __name__ == "__main__":
	keep_alive()

