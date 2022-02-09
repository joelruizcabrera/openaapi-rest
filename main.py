import flask
from flask import json
import json

with open("data/todo_lists.json") as jsonData:
    data = json.load(jsonData)
    jsonData.close()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/list/<id>', methods=['GET'])
def list_get(id):
    return "LIST GET " + id

@app.route('/list/<id>', methods=['DELETE'])
def list_delete(id):
    return "LIST DELETE " + id

@app.route('/list/', methods=['POST'])
def list_create():
    return "LIST CREATE"

@app.route('/list/<id>/entry', methods=['POST'])
def index(id):
    return "ENTRY ADD " + id

@app.route('/list/<id>/entry/<e_id>', methods=['POST'])
def index(id, e_id):
    return "ENTRY EDIT " + id + " : " + e_id

@app.route('/list/<id>/entry/<e_id>', methods=['DELETE'])
def index(id, e_id):
    return "ENTRY DELETE " + id + " : " + e_id

@app.route('/users', methods=['GET'])
def index():
    return "USERS GET"

@app.route('/user', methods=['POST'])
def index():
    return "USER ADD"

@app.route('/user/<u_id>', methods=['DELETE'])
def index(u_id):
    return "USER DELETE " + u_id

app.run()
