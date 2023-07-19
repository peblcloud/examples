import pebl
from flask import Flask, abort, request
from db import connect, Message


app = Flask(__name__)


@app.route("/create", methods=["POST"])
def create_message():
    data = request.get_json(force=True, silent=True) or {}
    if "message" not in data:
        abort(400)

    m = Message.create(content=data["message"])
    return {
        "message_id": m.mid
    }


@app.route("/")
def get_messages():
    messages = Message.select().order_by(Message.mid.desc())
    serialized = [
        {"mid": m.mid, "content": m.content}
        for m in messages
    ]
    return {
        "messages": serialized,
    }


def run():
    connect()
    pebl.service(app, "hey.pebl.rocks")
