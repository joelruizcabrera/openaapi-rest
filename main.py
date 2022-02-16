import flask
from flask import json, request
import json

import uuid

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/list/<id>', methods=['GET'])
def list_get(id):
    with open("data/todo_lists.json", 'r') as jsonData:
        data = json.load(jsonData)
        listEntrys = []
        for i in data["data"]:
            if i["tdListId"] == id:
                listEntrys.append(i)
        with open("data/all_lists.json") as jsonLists:
            lists = json.load(jsonLists)
            print(lists)
            return {
                "listId": id,
                "listEntrys": listEntrys,
                "listName": lists["data"][id]["listName"],
                "status": 200,
            }
            jsonLists.close()
        jsonData.close()


@app.route('/list/<id>', methods=['DELETE'])
def list_delete(id):
    return "LIST DELETE " + id

@app.route('/list', methods=['POST'])
def list_create():
    body = json.loads(request.data)
    if ("listName" not in body):
        err = error_handling(405, "'listName' is not defined")
        return err
    if ("userId" not in body):
        err = error_handling(405, "'userId' is not defined")
        return err

    with open('data/all_lists.json', 'r+') as jsonLists:
        tempData = json.load(jsonLists)
        jsonLists.seek(0)
        newId = str(uuid.uuid4())
        tempData["data"][newId] = {
            "listId": newId,
            "listName": body["listName"],
            "listOwner": body["userId"],
            "listEntrys": [],
        }
        print(tempData)
        json.dump(tempData, jsonLists, indent=4, separators=(',', ': '))

    return error_handling(200, "Successfully created list")

@app.route('/list/<id>/entry', methods=['POST'])
def entry_add(id):
    return "ENTRY ADD " + id

@app.route('/list/<id>/entry/<e_id>', methods=['POST'])
def entry_edit(id, e_id):
    return "ENTRY EDIT " + id + " : " + e_id

@app.route('/list/<id>/entry/<e_id>', methods=['DELETE'])
def entry_delete(id, e_id):
    return "ENTRY DELETE " + id + " : " + e_id

@app.route('/users', methods=['GET'])
def users_get():
    with open("data/users.json", 'r') as jsonData:
        data = json.load(jsonData)
        return data
        jsonData.close()

@app.route('/user', methods=['POST'])
def user_add():
    return "USER ADD"

@app.route('/user/<u_id>', methods=['DELETE'])
def user_delete(u_id):
    return "USER DELETE " + u_id



def error_handling(code, msg):
    return {
        "code": code,
        "message": msg
    }

app.run()
