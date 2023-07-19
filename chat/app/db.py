from peewee import *

import pebl
import pymysql


model_db = MySQLDatabase(None)


class Message(Model):
    mid = AutoField()
    content = CharField()

    class Meta:
        database = model_db


def connect():
    db = pebl.mysql("db")
    model_db.init(
        "chat",
        host=db["host"],
        port=db["port"],
        user=db["user"],
        password=db["password"])


def setup():
    db = pebl.mysql("db")

    conn = pymysql.connect(**db)
    conn.cursor().execute("CREATE DATABASE IF NOT EXISTS chat")
    conn.close()

    connect()
    model_db.create_tables([Message])
    model_db.close()
