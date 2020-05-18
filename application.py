import os
import requests
import simplejson as json
from flask import Flask, session, request, render_template, redirect, url_for, jsonify
from flask_session import Session

from helpers import best
from mtmgureak import shareOut

app = Flask(__name__)

@app.route("/", methods=["Get", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    else:
        values = []
        for key, val in request.form.items():
            if key.startswith("e"):
                values.append(int(val))
        takt_time = float(request.form.get("takt_time"))
        op = shareOut(values,takt_time)
        return render_template("results.html", op = op)
