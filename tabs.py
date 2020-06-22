
#imports
import pandas as pd
from bokeh.resources import INLINE
from bokeh.plotting import figure, show, curdoc
from bokeh.util.string import encode_utf8
from bokeh.transform import dodge
from math import pi
from bokeh.transform import cumsum
from bokeh.core.properties import value
from bokeh.models import ColumnDataSource, ColorBar, PrintfTickFormatter, NumeralTickFormatter, FactorRange, LabelSet, GeoJSONDataSource, LinearColorMapper, Tabs, Panel, HoverTool
from bokeh.transform import factor_cmap
from bokeh.models.widgets import Panel, Tabs
from bokeh.palettes import viridis
from bokeh.resources import CDN
from bokeh.embed import file_html


def maps():
    
    
    p16 = figure(x_axis_location = None, y_axis_location = None, match_aspect=True)
    p16.image_url(url=['/static/images/pp16s.png'], x=0, y=0, w=3, h=3, anchor="bottom_left")
    p16.title.align='center'    
    p16.grid.grid_line_color=None
    p16.outline_line_color=None
    p16.toolbar.autohide = True
    p16.title.text_font_style = "bold"
        
    p11 = figure(x_axis_location = None, y_axis_location = None, match_aspect=True)
    p11.image_url(url=['/static/images/pp11s.png'], x=0, y=0, w=3, h=3, anchor="bottom_left")
    p11.title.align='center'    
    p11.grid.grid_line_color=None
    p11.outline_line_color=None
    p11.toolbar.autohide = True
    p11.title.text_font_style = "bold"

    p06 = figure(x_axis_location = None, y_axis_location = None, match_aspect=True)
    p06.image_url(url=['/static/images/pp06s.png'], x=0, y=0, w=3, h=3, anchor="bottom_left")
    p06.title.align='center'    
    p06.grid.grid_line_color=None
    p06.outline_line_color=None
    p06.toolbar.autohide = True
    p06.title.text_font_style = "bold"

    p02 = figure(x_axis_location = None, y_axis_location = None, match_aspect=True)
    p02.image_url(url=['/static/images/pp02s.png'], x=0, y=0, w=3, h=3, anchor="bottom_left")
    p02.title.align='center'    
    p02.grid.grid_line_color=None
    p02.outline_line_color=None
    p02.toolbar.autohide = True
    p02.title.text_font_style = "bold"

    t02 = Panel(child=p02, title='2002')
    t06 = Panel(child=p06, title='2006')
    t11 = Panel(child=p11, title='2011')
    t16 = Panel(child=p16, title='2016')
    tabs = Tabs(tabs=[t16,t11,t06,t02])

    return tabs
