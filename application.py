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
        divisor = takt_time * (float(list(op.keys())[-1]) + 1)
        numerator = 0

        for v in (list(op.values())):
            print(v[1])
            numerator += v[1]

        equilibrado = (numerator/divisor) * 100
        print(numerator)
        print(divisor)

        return render_template("results.html", op = op, equilibrado = equilibrado)
