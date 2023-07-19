import pebl
import redis

from flask import Flask

res = pebl.redis("foo")
r = redis.Redis(**res)

app = Flask(__name__)

@app.route("/")
def root():
    return b"hello, world!\n"

@app.route("/incr")
def incr():
    res = r.incr("counter")
    return {
        "count": int(res)
    }

pebl.service(app, "hey.pebl.rocks")
