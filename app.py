import pandas as pd
import random
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.plotting import figure, show
from bokeh.util.string import encode_utf8
from bokeh.models import ColumnDataSource, HoverTool, PrintfTickFormatter, NumeralTickFormatter
from bokeh.transform import factor_cmap
from bokeh.palettes import viridis
from bokeh.resources import CDN
from bokeh.embed import file_html

from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/')
def bokeh():
    script, div = components(sample_plot())

    return render_template('bokeh.html', script=script, div=div)


def sample_plot():

    df = pd.read_csv('BokehApp/Data/houseStock1.csv')
    df = df[['Year', 'Dublin_Vacant', 'Irl_Vacant', 'Dublin_Total','Irl_Total']]
    df.columns = ['Year', 'Dublin vacant', 'Ireland vacant', 'Dublin', 'Ireland']
    ll = list(df.columns[1:])
    source = ColumnDataSource(data=dict(x=df.Year.values,y=df['Ireland'], y1=df['Dublin'], y2=df['Ireland vacant'], y3=df['Dublin vacant']))
    a2 = figure(plot_width=650, plot_height=400, title='Irish House Stock', tools = 'pan, wheel_zoom, box_zoom, reset, hover') #, tooltips=ToolTips)
    colors = viridis(4)
    a2.varea_stack(['y3','y2','y1','y'], x='x', source=source, color=colors[::-1], legend=ll, muted_alpha=0.2)
    a2.legend.location='top_left'
    a2.legend.click_policy="mute"
    a2.yaxis[0].formatter = NumeralTickFormatter(format="0 M")
    tick_labels = {'500000':'0.5M','1000000':'1M','1500000':'1,5M','2000000':'2M','2500000':'2,5M'}
    a2.yaxis.major_label_overrides = tick_labels
    a2.xaxis.ticker = df.Year.values
    return a2

