import os
import requests
import simplejson as json
from flask import Flask, session, request, render_template, redirect, url_for, jsonify
from flask_session import Session

from flask_googlecharts import GoogleCharts
from flask_googlecharts import LineChart

from helpers import best
from mtmgureak import shareOut

app = Flask(__name__)
charts = GoogleCharts(app)



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
        number_op = (float(list(op.keys())[- 1]) + 1)
        divisor = tiempo_ciclo * number_op
        numerator = 0

        for v in (list(op.values())):
            numerator += v[1]

        equilibrado = round((numerator / divisor) * 100, 2)

        # Make the data for the GRAPH
        data = []
        for key in op:
            new_data = []
            new_data.append(int(key) + 1 )
            new_data.append(op[key][1])
            new_data.append(tiempo_ciclo)
            data.append(new_data)

        # Declare the GRAPH and add the data
        my_chart = LineChart("my_chart", options={'title': 'Equilibrado'})

        my_chart.add_column("number", "Puesto")
        my_chart.add_column("number", "Operario")
        my_chart.add_column("number", "Tiempo de ciclo")
        my_chart.add_rows(data)


        charts.register(my_chart)


        return render_template("results.html", op = op, equilibrado = equilibrado, tiempo_ciclo = tiempo_ciclo, numerator = numerator, number_op = number_op)
