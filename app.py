from flask import Flask, render_template, request
from bokeh.embed import components
from plots1 import houseStockPlot, vacantPlot

app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/')
def bokeh():
    script, div = components(houseStockPlot())

    return render_template('bokeh.html', script=script, div=div)