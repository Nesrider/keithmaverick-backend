from flask import Flask,request, jsonify
from dbconnect import connection
import gc
import json

app = Flask(__name__)

#Takes the returned sql query and converts
#it into a dictionary format
def toDict(sqlData, Header, table_name):

	rows = []

	for i in xrange(len(sqlData)):
		row ={}

		for j in xrange(len(Header)):
			row[Header[j]] = sqlData[i][j]

		rows.append(row)

	return {table_name : rows}

#Takes a returned 
def getHeaders(sqlHeader):
	header = []

	for i in xrange(len(sqlHeader)):
		header.append(sqlHeader[i][0])

	return header

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

#Returns a JSON of a Table
def getTable(table_name):
	result = query("SELECT * FROM %s" % table_name)
	resultHeader = getHeaders(query("SHOW COLUMNS FROM %s" % table_name))
	return jsonify(toDict(result, resultHeader, table_name))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/projects', methods=["GET"])
def projects():
	return getTable("PROJECT")

@app.route('/images', methods=["GET"])
def images():
	return getTable("IMAGE")

@app.route('/subjects', methods=["GET"])
def subjects():
	return getTable("SUBJECT")



