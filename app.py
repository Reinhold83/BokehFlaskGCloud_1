from flask import Flask, render_template, request
from bokeh.embed import components
from plots1 import houseStockPlot, vacantPlot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oratoroeuaroupadoreideroma123'

#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/')
def bokeh():
    script, div = components(houseStockPlot())
    script1, div1 = components(vacantPlot())

    return render_template('bokeh.html', script=script, div=div, script1=script1, div1=div1)