# file name : app.py
from flask import Flask, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
 
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return 'hello world'
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
 
