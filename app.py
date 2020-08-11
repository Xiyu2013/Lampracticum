# importing the flask class from the flask module
import base64
import json
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

import plotly
from flask import Flask,render_template
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as plt

from flask import Flask, render_template, request, send_file
from matplotlib import pyplot as plt
import os
import sys

sys.path.append(os.path.abspath("/Users/ananyakondiparthy/lam/flaskr"))
# from modeling.scikit_learn.input_file import InputForm
# from modeling.scikit_learn.materials import compute
from modeling.scikit_learn.salesquantity import dfGeneral
# from blueprints.views import parts_blueprint
import modeling.scikit_learn.salesquantity
plt.style.use('ggplot')

app = Flask(__name__)


# using decorators to link the function to a URL
@app.route('/')
def index():
    headline = "Welcome to Lam Research Spare Parts Analysis"
    return render_template("index.html", headline=headline)


@app.route('/parts', methods=("POST", "GET"))
def html_table():
    return render_template('sales.html', tables= [dfGeneral.to_html(classes='data')], titles= dfGeneral.columns.values)


@app.route('/plot')
def html_table2(labelDate=None):
    fig,ax = plt.subplots()
    labelDate=dfGeneral.Quarter[3:len(dfGeneral):4]
    #plt.figure(figsize=(18,6))
    # plt.plot(dfGeneral.Quarter,dfGeneral.SalesQty,'o-')
    plt.plot(dfGeneral.Quarter, dfGeneral.SalesQty, color ='blue')
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(4))
    plt.vlines(x=labelDate, ymin=0,ymax=40,linestyle='--')
    plt.xlabel("Quarter")
    plt.ylabel("SalesQty")
    plt.title("The Line Chart")
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


#bokeh -










# @app.route('/materials', methods=['GET', 'POST'])
# def plots():
#     form = InputForm(request.form)
#     if request.method == 'GET' and form.validate():
#         result = compute(form.Materials.data)
#         return render_template("plots.html", result=result)
#     else:
#         return "error"

#input : part number
# app.register_blueprint(parts_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
