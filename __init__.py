from flask import Flask,request
from db import getTable, getById

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Keith Maverick - Backend'

@app.route('/projects/sub/<int:subject_id>', methods=["GET"])
def projectsBySubject(subject_id):
	return getById("PROJECT", "SUBJECT_ID", subject_id)

@app.route('/images/sub/<int:subject_id>', methods=["GET"])
def imagesBySubject(subject_id):
	return getById("IMAGE", "SUBJECT_ID", subject_id)

@app.route('/projects', methods=["GET"])
def projects():
	return getTable("PROJECT")

@app.route('/images', methods=["GET"])
def images():
	return getTable("IMAGE")

@app.route('/subjects', methods=["GET"])
def subjects():
	return getTable("SUBJECT")



