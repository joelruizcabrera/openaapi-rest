import flask
from flask import json, request
import json

from datetime import datetime

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
    with open('data/all_lists.json', 'r+') as jsonLists:
        tempData = json.load(jsonLists)
        jsonLists.seek(0)
        del tempData["data"][id]
        print(tempData)
        json.dump(tempData, jsonLists, indent=4, separators=(',', ': '))

    return error_handling(200, "Successfully created list")

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

@app.route('/list/<id>/entry/<e_id>', methods=['GET'])
def entry_get(id, e_id):
    with open('data/all_lists.json', 'r+') as jsonLists:
        tempData = json.load(jsonLists)
        jsonLists.seek(0)

        listEntrys = json.dumps(tempData["data"][id]["listEntrys"])

        if e_id in listEntrys:
            with open("data/todo_lists.json", 'r') as jsonEntry:
                data = json.load(jsonEntry)
                for i in data["data"]:
                    if int(i["tdId"]) == int(e_id):
                        i["status"] = 200
                        return i

        else:
            return error_handling(404, "Entry was not found in this list")

@app.route('/list/<id>/entry/<e_id>', methods=['POST'])
def entry_edit(id, e_id):
    return "ENTRY EDIT " + id + " : " + e_id

@app.route('/list/<id>/entry/<e_id>', methods=['DELETE'])
def entry_delete(id, e_id):
    return "ENTRY DELETE " + id + " : " + str(e_id)

@app.route('/users', methods=['GET'])
def users_get():
    with open("data/users.json", 'r') as jsonData:
        data = json.load(jsonData)
        return data
        jsonData.close()

@app.route('/user/<u_id>', methods=['GET'])
def user_get(u_id):
    with open("data/users.json", 'r') as jsonData:
        data = json.load(jsonData)
        if (data["data"][u_id]):
            return {
                "status": 200,
                "data": {
                    "userId": u_id,
                    "userFullName": data["data"][u_id]["userFullName"],
                    "userShortName": data["data"][u_id]["userShortName"],
                    "userAvatar": data["data"][u_id]["userAvatar"],
                    "userLists": data["data"][u_id]["userLists"],
                    "userFriends": data["data"][u_id]["userFriends"],
                    "userCreatedAt": data["data"][u_id]["userCreatedAt"]
                }
            }
        jsonData.close()

@app.route('/user', methods=['POST'])
def user_add():
    body = json.loads(request.data)
    if "userFullName" not in body:
        return error_handling(405, "'userFullName' is not defined")
    if "userShortName" not in body:
        return error_handling(405, "'userShortName' is not defined")
    if "userAvatar" not in body:
        body["userAvatar"] = "/cdn/avatars/default.jpg?s=500x500"

    body["userCreatedAt"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    body["userFriends"] = []
    body["userLists"] = []

    with open("data/users.json", 'r+') as jsonUsers:
        tempData = json.load(jsonUsers)
        jsonUsers.seek(0)
        newId = str(uuid.uuid4())
        tempData["data"][newId] = body

        json.dump(tempData, jsonUsers, indent=4, separators=(',', ': '))

    return error_handling(200, {
        "msg": "user was successfully created",
        "userInfo": {
            "userId": newId,
            "userShortName": tempData["data"][newId]["userShortName"]
        }
    })

@app.route('/user/<u_id>', methods=['DELETE'])
def user_delete(u_id):
    return "USER DELETE " + u_id

def error_handling(code, msg):
    return {
        "status": code,
        "message": msg
    }

app.run()
