import os
from flask import Flask, request, Markup

app = Flask(__name__)

person = {}



@app.route("/")
def index():
    return "Hello World"

@app.route("/signup")
def register():
    html = """
    <form action="/signup">
        <p><label>ID(nick name): </label>
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
                    "nickname": ""
                    }
                    }
        person_id = request.form["id"]
        person_pass = request.form["pass"]
        if person_id not in person:
            person[person_id] = {"pass":person_pass}
            success_msg["user_id"] = person_id
            success_msg["nickname"] = person_id
            return success_msg,200
        else:

        
    else:
        return "" ,204



if __name__ == "__main__":
    app.run(debug=True)