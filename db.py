from flask import jsonify
from dbconnect import connection

import gc
import json


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

def openConnection():
	try:
		c, conn = connection()
		return c, conn
	except Exception as e:
		return (str(e))

def closeConnection(c, conn):
	c.close()
	conn.close()
	gc.collect
	return

def query(c, statement):
	try: 
		allSubjects = c.execute(statement)
		queryResult = c.fetchall()
		return queryResult

	except Exception as e:
		return(str(e))

#Returns a JSON of a Table
def getTable(table_name):
	c, conn = openConnection()
	result = query(c, "SELECT * FROM %s" % table_name)
	resultHeader = getHeaders(
		query(c, "SHOW COLUMNS FROM %s" % table_name))
	closeConnection(c, conn)
	return jsonify(toDict(result, resultHeader, table_name))


def getById(table_name, id_name, id_value):
	c, conn = openConnection()
	result = query(c, "SELECT * FROM %s WHERE %s = %d" % 
		(table_name, id_name, id_value))
	resultHeader = getHeaders(
		query(c, "SHOW COLUMNS FROM %s" % table_name))
	closeConnection(c, conn)
	return jsonify(toDict(result, resultHeader, table_name))

	