from flask import Flask
from dbconnect import connection


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/subjects', methods=["GET"])
def subjects():
	try: 
		c, conn = connection()
		return ("okay!")
	except Exception as e:
		return(str(e))