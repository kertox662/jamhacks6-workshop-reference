from flask import Flask, request
from flask_restful import Api, Resource
import sys, json

app = Flask(__name__)
api = Api(app)

dbFile = "jams.json"
if len(sys.argv) >= 2:
    dbFile = sys.argv[1]

jamDB = {}

def loadDB():
    global jamDB
    with open(dbFile) as file:
        jamDB = json.load(file)

def saveDB():
    with open(dbFile, "w") as file:
        json.dump(jamDB, file, indent=4)

class DatabaseIO(Resource):
    def post(self, action):
        if action == "load":
            try:
                loadDB()
            except FileNotFoundError:
                return {"message":"error: database file not found"}, 500
            except json.JSONDecodeError:
                return {"message":"error: database file decode error"}, 500
            return {"message":"SUCCESS"}

        elif action == "save":
            try:
                saveDB()
            except Exception as e:
                return {"message": f"error: could not save database, {e}"}, 500
            return {"message":"SUCCESS"}

        else:
            return {"message": f"error: invalid endpoint {action}"}, 400
        

class Jams(Resource):
    def get(self, flavour=None):
        if flavour is None:
            return {"data": list(jamDB.keys())}

        if flavour not in jamDB:
            return {"message": f"error: we do not have the flavour {flavour}"}, 404
        
        return {
            "data": {
                "flavour": flavour,
                "amount": jamDB[flavour]
            }
        }

    def patch(self, flavour=None):
        if flavour not in jamDB:
            return {"message": f"error: we do not have the flavour {flavour}"}, 404
        
        if "action" not in request.args:
            return {"message": f"error: no action specified in query parameters, use either 'eat' or 'buy'"}, 400
        action = request.args["action"]

        if action == "eat":
            if jamDB[flavour] > 0:
                jamDB[flavour] -= 1
                return {
                    "message": f"Ate one {flavour} jam!",
                    "data": {
                        "flavour": flavour,
                        "amount": jamDB[flavour]
                    }
                }
            else:
                return {"message": f"error: we do not have any {flavour} jam left!"}, 400

        elif action == "buy":
            jamDB[flavour] += 1
            return {
                "message": f"Bought one {flavour} jam!",
                "data": {
                    "flavour": flavour,
                    "amount": jamDB[flavour]
                }
            }

        else:
            {"message": f"error: unknown action {action}, use either 'eat' or 'buy'"}, 400

api.add_resource(Jams, "/jam","/jam/<string:flavour>")
api.add_resource(DatabaseIO, "/db/<string:action>")

if __name__ == "__main__":
    try:
        loadDB()
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print("Error reading Database file:")
        print(e)
        exit()
    app.run(host="0.0.0.0", port=8000)