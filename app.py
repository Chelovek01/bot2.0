import json
import time
import os
import sys
from flask import Flask, request

import config
from handler import *


sys.path.append('/home/bot/bot2.0/env/lib/python3.6/site-packages/')
app = Flask(__name__)


def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp


@app.route("/webhook")
def webhook():
    try:
        if request.method == "POST":
            data = request.get_json()
            key = data["key"]
            if key == config.sec_key:
                print(get_timestamp(), "Alert Received & Sent!")
                send_alert(data)
                return "Sent alert", 200

            else:
                print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
                return "Refused alert", 400

    except Exception as e:
        print("[X]", get_timestamp(), "Error:\n>", e)
        return "Error", 400

    return 'aptapta'

if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=80)
