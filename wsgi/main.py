from pebl import wsgi_run
from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def root():
    return "hello, world!"


@app.route("/echo", methods=["POST"])
def echo():
    return request.get_data()


wsgi_run(app, "hey.pebl.rocks")
