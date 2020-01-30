import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.models import ColumnDataSource, HoverTool, PrintfTickFormatter
from bokeh.transform import factor_cmap

from flask import Flask, render_template, request




@app.route('/')
def index():

    df = pd.read_csv('BokehApp/Data/houseStock.csv')

    return render_template("index.html")
