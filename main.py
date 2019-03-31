import os
from flask import Flask, request, Markup

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/signup")
def register():
    html = """
    <form action="/signup">
        <p><label>test: </label>
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
        return request.form["id"]
    else:
        return "" ,204



if __name__ == "__main__":
    app.run(debug=True)