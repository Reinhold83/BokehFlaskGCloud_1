#imports
import pandas as pd
from bokeh.resources import INLINE
from bokeh.plotting import figure, show
from bokeh.util.string import encode_utf8
from bokeh.transform import dodge
from bokeh.core.properties import value
from bokeh.models import ColumnDataSource, HoverTool, PrintfTickFormatter, NumeralTickFormatter, FactorRange
from bokeh.transform import factor_cmap
from bokeh.palettes import viridis
from bokeh.resources import CDN
from bokeh.embed import file_html

#Functions/Plots
def vacantPlot():
    dfvt = pd.read_csv('BokehApp/Data/HousesVacants.csv', delimiter='\t', header=0)
    
    dfvt = dfvt.iloc[:4]
    dfv = dfvt[['Type', 'Dublin city & suburbs','Rural']]
    dfv['Other cities'] = dfvt.iloc[:, 2:-2].sum(axis=1)
    dfv.set_index('Type', inplace=True)
    dfv.columns = ['Dublin&Suburbs', 'Rural', 'Other cities']
    dfv = dfv[['Dublin&Suburbs', 'Other cities', 'Rural']]
    rowX = dfv.index.values[::]
    xLabel = ['Dublin', 'Other cities', 'Rural']
    lDict = {'For Sale': xLabel, 'Deceased':xLabel, 'Vacant Long Term':xLabel, 'Rental Property':xLabel}
    source = ColumnDataSource(data=dict(x= list(dfv.index.values), y=dfv['Dublin&Suburbs'], y1=dfv['Other cities'], y2=dfv['Rural']))

    p = figure(x_range=FactorRange(*lDict), plot_height=350, plot_width=550, title='Vacant properties in Ireland 2016', x_axis_label=None, y_axis_label='amount of vacant properties')
    hover = HoverTool()
    hover.tooltips=[('Vacant properties', 'Dublin @y / Others @y1 / Rural @y2')]
    p.add_tools(hover)
    
    p.vbar(x=dodge('x', -0.25, range=p.x_range), top='y', width=0.2, source=source, color='#FDE724', legend=value('Dublin&Suburbs'))
    p.vbar(x=dodge('x', 0.0, range=p.x_range), top='y1', width=0.2, source=source, color='#208F8C', legend=value('Other cities'))
    p.vbar(x=dodge('x', 0.25, range=p.x_range), top='y2', width=0.2, source=source, color='#440154', legend=value('Rural'))
    tick_labels = {'1000':'1K','2000':'2K','3000':'3K','4000':'4K','5000':'5K'}
    p.yaxis.major_label_overrides = tick_labels
    p.legend.location= 'top_right'#(370,180)
    p.legend.background_fill_alpha=None
    p.legend.border_line_alpha=0
    p.legend.label_text_font_size = "9px"
    p.y_range.end = dfv.values.max()*1.1+1
    p.legend.click_policy="hide"
    p.title.text_font_size = '15px'
    p.xaxis.major_label_text_font_style = 'bold'
    p.grid.grid_line_color=None
    p.toolbar.autohide = True
    return p


def houseStockPlot():
    
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

