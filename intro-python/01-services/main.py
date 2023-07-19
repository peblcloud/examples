import pebl
from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
  return "Hello!"

@app.route("/ping")
def ping():
  return "pong"

pebl.service(app, "example.com")
