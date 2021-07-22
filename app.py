#!/usr/bin/python

import time
from flask import Flask
app = Flask(__name__)

import pymongo
from pymongo import MongoClient
import urllib.parse
username = "rnwuser"
password = "Irg@370ahmz"
client = pymongo.MongoClient('mongodb://{username}:{urrllib.parse.quote_plus(password)}@192.168.136.130:27017/Production')
mydb = client["Production"]
information = mydb["jiten"]
record = [{"name": "Krishna", "age": 27},{"name": "Shanti", "age": 50}]
information.insert_many(record)
print(client.list_database_names())


START = time.time()

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

@app.route('/')
def root():
    return "Hello World (Python)! (up %s)\n" % elapsed()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4030)
