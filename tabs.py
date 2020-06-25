
#imports
import pandas as pd
from bokeh.resources import INLINE
from bokeh.plotting import figure, show, curdoc
from bokeh.util.string import encode_utf8
from bokeh.transform import dodge
from math import pi
from bokeh.transform import cumsum
from bokeh.layouts import column, row, gridplot
from bokeh.core.properties import value
from bokeh.models import ColumnDataSource, ColorBar, PrintfTickFormatter, NumeralTickFormatter, FactorRange, LabelSet, GeoJSONDataSource, LinearColorMapper, Tabs, Panel, HoverTool, Div
from bokeh.transform import factor_cmap
from bokeh.models.widgets import Panel, Tabs
from bokeh.palettes import viridis
from bokeh.resources import CDN
from bokeh.embed import file_html


def maps():
    
    
    p16 = figure(x_axis_location = None, y_axis_location = None, match_aspect=True, plot_width=600)
    p16.image_url(url=['/static/images/pp16s.png'], x=0, y=0, w=3, h=3, anchor="bottom_left")
    p16.title.align='center'    
    p16.grid.grid_line_color=None
    p16.outline_line_color=None
    p16.toolbar.autohide = True
    p16.title.text_font_style = "bold"
        
    p11 = figure(x_axis_location = None, y_axis_location = None, match_aspect=True, plot_width=600)
    p11.image_url(url=['/static/images/pp11s.png'], x=0, y=0, w=3, h=3, anchor="bottom_left")
    p11.title.align='center'    
    p11.grid.grid_line_color=None
    p11.outline_line_color=None
    p11.toolbar.autohide = True
    p11.title.text_font_style = "bold"

    p06 = figure(x_axis_location = None, y_axis_location = None, match_aspect=True, plot_width=600)
    p06.image_url(url=['/static/images/pp06s.png'], x=0, y=0, w=3, h=3, anchor="bottom_left")
    p06.title.align='center'    
    p06.grid.grid_line_color=None
    p06.outline_line_color=None
    p06.toolbar.autohide = True
    p06.title.text_font_style = "bold"

    p02 = figure(x_axis_location = None, y_axis_location = None, match_aspect=True, plot_width=600)
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


def ageGroup():

    df = pd.read_csv('BokehApp/Data/popByAgeGroup_v2.csv', delimiter=',', index_col='AgeGroup')
    df_pivot1 = df.pivot_table(values=['2002','2003','2004','2005','2006','2007', '2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'],index='sex', columns='AgeGroup')
    

    ys= list(df.index.unique())
    source = ColumnDataSource(data=dict(y=ys,x02f=df_pivot1.loc['female']['2002'],x02m=df_pivot1.loc['male']['2002'],x06f=df_pivot1.loc['female']['2006'],x06m=df_pivot1.loc['male']['2006'], x11f=df_pivot1.loc['female']['2011'],x11m=df_pivot1.loc['male']['2011'],x16f=df_pivot1.loc['female']['2016'],x16m=df_pivot1.loc['male']['2016']))

    #plot fig left
    p = figure(y_axis_location = None, match_aspect=True, y_range=ys)
    p.hbar(y="y", height=1, right='x02m', legend=value('male'),source=source, line_color="white", fill_color='#FDE724')

    #plot style
    hoverp = HoverTool()
    hoverp.tooltips=[('Population', '@x02m')]
    p.add_tools(hoverp)
    p.x_range.flipped = True
    p.grid.grid_line_color=None
    p.outline_line_color=None
    p.x_range.range_padding = 0
    p.axis.major_label_text_font_style = 'bold'
    p.toolbar.autohide = True
    p.axis.axis_line_color = None
    p.legend.location = 'top_left'
    p.legend.background_fill_alpha = None
    p.legend.border_line_color = None


    #plot fig right
    #y02max, y02min = df_pivot1.loc['female']['2002'].max(), df_pivot1.loc['female']['2002'].min()
    p1 = figure(match_aspect=True, y_range=ys)
    p1.hbar(y="y", height=1, right='x02f', legend=value('female'), source=source, line_color="white", fill_color='#440154')

    hoverp1 = HoverTool()
    hoverp1.tooltips=[('Population', '@x02f')]

    #plot style
    p1.add_tools(hoverp1)
    p1.legend.background_fill_alpha = None
    p1.legend.border_line_color = None
    p1.yaxis.major_label_standoff = -1
    p1.yaxis.major_label_text_font_size = '8pt'
    p1.grid.grid_line_color=None
    p1.outline_line_color=None
    p1.yaxis.major_label_text_align = 'center'
    p1.axis.major_label_text_font_style = 'bold'
    p1.yaxis.major_tick_line_color = None
    p1.axis.axis_line_color = None
    p1.min_border = 0
    p1.x_range.range_padding = 0
    p1.toolbar.autohide = True
    p1.yaxis.major_label_standoff = 0



    #plot fig left
    p6m = figure(y_axis_location = None, match_aspect=True, y_range=ys)
    p6m.hbar(y="y", height=1, right='x06m', legend=value('male'), source=source, line_color="white", fill_color='#FDE724')

    #plot style
    hoverp6m = HoverTool()
    hoverp6m.tooltips=[('Population', '@x06m')]
    p6m.add_tools(hoverp6m)
    p6m.x_range.flipped = True
    p6m.grid.grid_line_color=None
    p6m.outline_line_color=None
    p6m.x_range.range_padding = 0
    p6m.axis.major_label_text_font_style = 'bold'
    p6m.toolbar.autohide = True
    p6m.axis.axis_line_color = None
    p6m.legend.location = 'top_left'
    p6m.legend.background_fill_alpha = None
    p6m.legend.border_line_color = None


    #plot fig right
    p6f = figure(match_aspect=True, y_range=ys)
    p6f.hbar(y="y", height=1, right='x06f', legend=value('female'), source=source, line_color="white", fill_color='#440154')

    hoverp6f = HoverTool()
    hoverp6f.tooltips=[('Population', '@x06f')]

    #plot style
    p6f.add_tools(hoverp6f)
    p6f.legend.background_fill_alpha = None
    p6f.legend.border_line_color = None
    p6f.yaxis.major_label_standoff = -1
    p6f.yaxis.major_label_text_font_size = '8pt'
    p6f.grid.grid_line_color=None
    p6f.outline_line_color=None
    p6f.yaxis.major_label_text_align = 'center'
    p6f.axis.major_label_text_font_style = 'bold'
    p6f.yaxis.major_tick_line_color = None
    p6f.axis.axis_line_color = None
    p6f.min_border = 0
    p6f.x_range.range_padding = 0
    p6f.toolbar.autohide = True
    p6f.yaxis.major_label_standoff = 0

    #plot fig left
    p11m = figure(y_axis_location = None, match_aspect=True, y_range=ys)
    p11m.hbar(y="y", height=1, right='x11m', legend=value('male'), source=source, line_color="white", fill_color='#FDE724')
    hoverp11m = HoverTool()
    hoverp11m.tooltips=[('Population', '@x11m')]
    p11m.add_tools(hoverp11m)

    #plot style
    p11m.x_range.flipped = True
    p11m.grid.grid_line_color=None
    p11m.outline_line_color=None
    p11m.x_range.range_padding = 0
    p11m.axis.major_label_text_font_style = 'bold'
    p11m.toolbar.autohide = True
    p11m.axis.axis_line_color = None
    p11m.legend.location = 'top_left'
    p11m.legend.background_fill_alpha = None
    p11m.legend.border_line_color = None


    #plot fig right
    p11f = figure(match_aspect=True, y_range=ys)
    p11f.hbar(y="y", height=1, right='x11f', legend=value('female'), source=source, line_color="white", fill_color='#440154')

    hoverp11f = HoverTool()
    hoverp11f.tooltips=[('Population', '@x11f')]
    p11f.add_tools(hoverp11f)

    #plot style
    p11f.legend.background_fill_alpha = None
    p11f.legend.border_line_color = None
    p11f.yaxis.major_label_standoff = -1
    p11f.yaxis.major_label_text_font_size = '8pt'
    p11f.grid.grid_line_color=None
    p11f.outline_line_color=None
    p11f.yaxis.major_label_text_align = 'center'
    p11f.axis.major_label_text_font_style = 'bold'
    p11f.yaxis.major_tick_line_color = None
    p11f.axis.axis_line_color = None
    p11f.min_border = 0
    p11f.x_range.range_padding = 0
    p11f.toolbar.autohide = True
    p11f.yaxis.major_label_standoff = 0


    #plot fig left
    p16m = figure(y_axis_location = None, match_aspect=True, y_range=ys)
    p16m.hbar(y="y", height=1, right='x16m', legend=value('male'), source=source, line_color="white", fill_color='#FDE724')
    hoverp16m = HoverTool()
    hoverp16m.tooltips=[('Population', '@x16m')]
    p16m.add_tools(hoverp16m)

    #plot style
    
   
    p16m.x_range.flipped = True
    p16m.grid.grid_line_color=None
    p16m.outline_line_color=None
    p16m.x_range.range_padding = 0
    p16m.axis.major_label_text_font_style = 'bold'
    p16m.toolbar.autohide = True
    p16m.axis.axis_line_color = None
    p16m.legend.location = 'top_left'
    p16m.legend.background_fill_alpha = None
    p16m.legend.border_line_color = None


    #plot fig right
    p16f = figure(match_aspect=True, y_range=ys)
    p16f.hbar(y="y", height=1, right='x16f', legend=value('female'), source=source, line_color="white", fill_color='#440154')

    hoverp16f = HoverTool()
    hoverp16f.tooltips=[('Population', '@x16f')]
    p16f.add_tools(hoverp16f)

    #plot style
    #p16m.title_location = 'above'
    #p16m.title.align = 'left'
    #p16m.title.text_font_size = '12pt'
    #p16m.title.text_font_style = 'bold'


    p16f.legend.background_fill_alpha = None
    p16f.legend.border_line_color = None
    p16f.yaxis.major_label_standoff = -1
    p16f.yaxis.major_label_text_font_size = '8pt'
    p16f.grid.grid_line_color=None
    p16f.outline_line_color=None
    p16f.yaxis.major_label_text_align = 'center'
    p16f.axis.major_label_text_font_style = 'bold'
    p16f.yaxis.major_tick_line_color = None
    p16f.axis.axis_line_color = None
    p16f.min_border = 0
    p16f.x_range.range_padding = 0
    p16f.toolbar.autohide = True
    p16f.yaxis.major_label_standoff = 0



    #Divs for griplot

    #Gridplots
    p02 = gridplot([[p, p1]], plot_width=350, toolbar_location='right', merge_tools=True)   
    p06 = gridplot([[p6m, p6f]], plot_width=350, toolbar_location='right', merge_tools=True)
    p11 = gridplot([[p11m, p11f]], plot_width=350, toolbar_location='right', merge_tools=True)
    p16 = gridplot([[p16m, p16f]], plot_width=350, toolbar_location='right', merge_tools=True)



    #Tabs
    t02 = Panel(child=p02, title='2002')
    t06 = Panel(child=p06, title='2006')
    t11 = Panel(child=p11, title='2011')
    t16 = Panel(child=p16, title='2016')
    tabs = Tabs(tabs=[t16,t11,t06,t02])


    return tabs
