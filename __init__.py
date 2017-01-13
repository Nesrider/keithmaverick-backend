from flask import Flask,request, Response
from db import getTable, getById, addCor
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

#from flask_cors import CORS, cross_origin
app = Flask(__name__)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
#@cross_origin()
def hello_world():
  return 'Keith Maverick - Backend'

@app.route('/projects/sub/<int:subject_id>', methods=["GET"])
#@cross_origin()
def projectsBySubject(subject_id):
	resp = addCor(getById("PROJECT", "SUBJECT_ID", subject_id))
	resp.status_code = 200
	return resp

@app.route('/images/sub/<int:subject_id>', methods=["GET"])
#@cross_origin()
def imagesBySubject(subject_id):
	resp = addCor(getById("IMAGE", "SUBJECT_ID", subject_id))
	resp.status_code = 200
	return resp

@app.route('/projects', methods=["GET"])
#@cross_origin()
def projects():
	resp = addCor(getTable("PROJECT"))
	resp.status_code = 200
	return resp

@app.route('/images', methods=["GET"])
#@cross_origin()
def images():
	resp = addCor(getTable("IMAGE"))
	resp.status_code = 200
	return resp

@app.route('/subjects', methods=["GET"])
#@cross_origin()
def subjects():
	print("\nRequest Recieved\n")

	resp = addCor(getTable("SUBJECT"))
	resp.status_code = 200
	return resp

if __name__ == "__main__":
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(5000)
	IOLoop.instance().start()
  #app.run(threaded=True)


