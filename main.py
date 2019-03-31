import os
from flask import Flask, request, Markup

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/signup")
def register():
    html = """
    <form action="/test">
        <p><label>test: </label>
        <input type="text" name="test" value="aaaa">
        <input type="text" name="pass" value="0000"
        <button type="submit" formmethod="post">POST</button></p>
    </form>
    """
    return Markup(html)

@app.rout("/signup",methods=["POST"])
def add_person():
    print(request.get_jason())
    return "",204



if __name__ == "__main__":
    app.run(debug=True)