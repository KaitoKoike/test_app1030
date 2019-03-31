import os
from flask import Flask, request, Markup
import json

app = Flask(__name__)

person = {"TaroYamada":{
            "password": "PaSSwd4TY",
            "nickname": "たろー",
            "comment": "僕は元気です"}
}


@app.route("/")
def index():
    return "",404

@app.route("/signup")
def register():
    html = """
    <form action="/signup">
        <p><label>ID: </label>
        <input type="text" name="id" value="aaaa"> </br>
        <label>pass: </label>
        <input type="text" name="pass" value="0000">
        <button type="submit" formmethod="post">Sign UP</button></p>
    </form>
    """
    return Markup(html)

@app.route("/signup",methods=["POST"])

def add_person():
    if request.method == "POST":
        success_msg = {
                    "message": "Account successfully created",
                    "user": {
                    "user_id": "",
                    }
                    }
        person_id = request.form["id"]
        person_pass = request.form["pass"]
        if person_id not in person:
            person[person_id] = {"pass":person_pass}
            success_msg["user"]["user_id"] = person_id
            success_msg["user"]["nickname"] = person_nick
            print(person)
            return json.dumps(success_msg),200
        else:
            error_msg = {
                "message": "Account creation failed",
                "cause": "required user_id and password"
                }
            return json.dumps(error_msg),400
    else:
        return "" ,204

@app.route("/users",methods=["GET"])
def get_person():
    person_id, person_pass = request.heaers["Authorization"].split(":")
    if person_id in person and person[person_id]["password"] == person_pass:
        success_msg = {
        "message": "User details by user_id",
        "user": {
        "user_id": "TaroYamada",
        "nickname": "",
        "comment": ""
            }
        }
        success_msg["user_id"] = person_id
        if person[person_id]["nickname"]:
            success_msg["nickname"] = person[person_id]["nickname"]
        else:
            success_msg["nickname"] = person[person_id]
        if person[person_id]["comment"]:
            success_msg["comment"] = person[person_id]["comment"]
        return json.dumps(success_msg),200
    else:
        error_msg = { "message":"Authentication Faild" }
        return json.dumps(error_msg) , 401


if __name__ == "__main__":
    app.run(debug=True)