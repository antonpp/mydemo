from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    country = request.args.get("country")
    return "Welcome to {}!".format(country)

if __name__ == "__main__":
    app.run(port=8080)