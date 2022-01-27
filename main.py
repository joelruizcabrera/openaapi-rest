import flask
from flask import json
import json

with open("data/todo_lists.json") as jsonData:
    data = json.load(jsonData)
    jsonData.close()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/list/get/<id>', methods=['GET'])
def index(id):

    list = {"data": {}}
    for i in data["data"]:
        objId = data["data"][i]["tdListId"]
        if id == objId:
            list["data"] = data["data"][i]
    return list


app.run()
