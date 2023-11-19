from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get("name", "World")
    return "Hello {}!!!!".format(name)

if __name__ == "__main__":
    app.run(port=8080)