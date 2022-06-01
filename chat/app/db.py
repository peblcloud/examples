import pebl
import flask
from peewee import *
import pymysql


model_db = MySQLDatabase(None)


class Message(Model):
    mid = AutoField()
    content = CharField()

    class Meta:
        database = model_db


def connect():
    db = pebl.mysql("db")
    model_db.init("chat", unix_socket=db.unix_socket, user=db.user)


def setup():
    db = pebl.mysql("db")

    conn = pymysql.connect(unix_socket=db.unix_socket, user=db.user)
    conn.cursor().execute("CREATE DATABASE IF NOT EXISTS chat")
    conn.close()

    model_db.init("chat", unix_socket=db.unix_socket, user=db.user)
    model_db.create_tables([Message])
    model_db.close()
