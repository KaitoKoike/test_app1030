import os
from flask import Flask, request, Markup ,render_template
import json

app = Flask(__name__)

person = {"kaito":{
            "password": "kaikaipoteto",
            "nickname": "コケ",
            "comment": "僕は元気です"}
}


@app.route("/")
def index():
    html = "<h1>hello world ! </h1>"
    return Markup(html)

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
        if (person_id not in person) and (person_id and person_pass):
            person[person_id] = {"pass":person_pass}
            success_msg["user"]["user_id"] = person_id
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

@app.route("/users/<user_id>",methods=["GET"])
def get_person(user_id = None):
    user_id = user_id
    person_id, person_pass = request.headers["Authorization"].split(":")
    print(person_id,person_pass)
    if person_id in person and person[person_id]["password"] == person_pass:
        success_msg = {
        "message": "User details by user_id",
        "user": {
        "user_id": "TaroYamada",
        "nickname": ""
            }
        }
        success_msg["user"]["user_id"] = person_id
        if person[person_id]["nickname"]:
            success_msg["user"]["nickname"] = person[person_id]["nickname"]
        else:
            success_msg["user"]["nickname"] = person[person_id]
        if person[person_id]["comment"]:
            success_msg["user"]["comment"] = person[person_id]["comment"]
        return json.dumps(success_msg),200
    else:
        error_msg = { "message":"Authentication Faild" }
        return json.dumps(error_msg) , 401




if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))