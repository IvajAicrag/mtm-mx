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
        tiempo_ciclo = float(request.form.get("takt_time"))
        factor = float(request.form.get("factor"))
        op = shareOut(values,tiempo_ciclo, factor)
        number_op = (float(list(op.keys())[-1]) + 1)
        divisor = tiempo_ciclo * number_op
        numerator = 0

        for v in (list(op.values())):
            numerator += v[1]

        equilibrado = (numerator/divisor) * 100


        return render_template("results.html", op = op, equilibrado = equilibrado, tiempo_ciclo = tiempo_ciclo, numerator = numerator, number_op = number_op)
