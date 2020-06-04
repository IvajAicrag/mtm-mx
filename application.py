import os
import requests
import simplejson as json
from flask import Flask, session, request, render_template, redirect, url_for, jsonify
from flask_session import Session

from flask_googlecharts import GoogleCharts
from flask_googlecharts import LineChart

from helpers import best
from mtmgureak import shareOut, shareOut_multiple

app = Flask(__name__)
charts = GoogleCharts(app)



@app.route("/", methods=["Get", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    else:
        multiples = False
        values = []
        tipos_op =[]
        for key, val in request.form.items():
            #take values from mtm table
            if key.startswith("e"):

                values.append(int(val))
            #take the quantity of operarios
            if key.startswith("op"):

                tipos_op.append(int(val))

        tiempo_ciclo = float(request.form.get("takt_time"))
        factor = float(request.form.get("factor"))

        #Do the analysis if the option of tipos de operarios was not selected
        if sum(tipos_op) == 0:

            op = shareOut(values,tiempo_ciclo, factor)
        else:

            op = shareOut_multiple(values,tiempo_ciclo, tipos_op)
            dic_factores = {1:"A", 0.91:"B", 0.83:"C1.1", 0.77:"C"}
            #Change factors to letters
            for fact in range(len(op)):
                op[fact][2] = dic_factores[op[fact][2]]
            op_request = sum(tipos_op)
            extras = len(op) - op_request
            if extras < 0:
                faltantes = abs(extras)
                extras = 0
                
            else:
                faltantes = 0
            multiples = True


        number_op = (int(list(op.keys())[- 1]) + 1)
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

        if multiples:

            return render_template("results_multi.html", op = op, equilibrado = equilibrado, tiempo_ciclo = tiempo_ciclo, numerator = numerator, number_op = number_op, faltantes = faltantes, extras = extras)

        else:
            return render_template("results.html", op = op, equilibrado = equilibrado, tiempo_ciclo = tiempo_ciclo, numerator = numerator, number_op = number_op)
