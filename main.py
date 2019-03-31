import os
from flask import Flask, request, Markup

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/signup",methods=["POST"])
def register():
    html = """
    <form action="/test">
        <p><label>test: </label>
        <input type="text" name="test" value="default">
        <button type="submit" formmethod="post">POST</button></p>
    </form>
    """
    return Markup(html)


if __name__ == "__main__":
    app.run(debug=True)