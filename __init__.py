from flask import Flask,request
from dbconnect import connection
import gc
import json

app = Flask(__name__)

def toJSON(sqlData, sqlHeader):

	for i in xrange(len(sqlObject)):
		for j in xrange(len(sqlObject[i])):

			return 0

def query(statement):
	try: 
		c, conn = connection()
		allSubjects = c.execute(statement)
		queryResult = c.fetchall()

		c.close()
		conn.close()
		gc.collect()

		return queryResult

	except Exception as e:
		return(str(e))


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/subjects', methods=["GET"])
def subjects():
	result = query("SELECT * FROM `SUBJECT`")
	resultHeader = query("SELECT * FROM `INFORMATION_SCHEMA`.`COLUMNS`")
	return str(result)