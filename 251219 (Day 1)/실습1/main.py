from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello!!!!"

@app.route("/user/<username>")
def greet(username):
    return f"{username}님, 환영합니다!"

if __name__ == "__main__":
    app.run(debug=True)