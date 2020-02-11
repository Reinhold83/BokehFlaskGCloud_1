#imports
import pandas as pd
from bokeh.resources import INLINE
from bokeh.plotting import figure, show, curdoc
from bokeh.util.string import encode_utf8
from bokeh.transform import dodge
from bokeh.core.properties import value
from bokeh.models import ColumnDataSource, HoverTool, PrintfTickFormatter, NumeralTickFormatter, FactorRange
from bokeh.transform import factor_cmap
from bokeh.models.widgets import Panel, Tabs
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

    p = figure(x_range=FactorRange(*lDict), plot_height=350, plot_width=550, title='Vacant properties in Ireland 2016', x_axis_label=None, y_axis_label='amount of vacant properties', tools = 'pan, wheel_zoom, box_zoom, reset')
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
    p.legend.label_text_font_size = "11px"
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
    a2 = figure(plot_width=550, plot_height=350, title='Irish House Stock', tools = 'pan, wheel_zoom, box_zoom, reset') #, tooltips=ToolTips)
    hover = HoverTool()
    hover.tooltips=[('Ireland', '@y'), ('Dublin','@y1'), ('Ireland vancant', '@y2'), ('Dublin vacant','@y3')]
    a2.add_tools(hover)
    
    colors = viridis(4)
    a2.varea_stack(['y3','y2','y1','y'], x='x', source=source, color=colors[::-1], legend=ll, muted_alpha=0.2)
    a2.legend.location='top_left'
    a2.legend.click_policy="mute"
    a2.yaxis[0].formatter = NumeralTickFormatter(format="0 M")
    tick_labels = {'500000':'0.5M','1000000':'1M','1500000':'1,5M','2000000':'2M','2500000':'2,5M'}
    a2.yaxis.major_label_overrides = tick_labels
    a2.xaxis.ticker = df.Year.values
    a2.title.text_font_size = '15px'
    a2.legend.background_fill_alpha=None
    a2.legend.border_line_alpha=0
    a2.legend.label_text_font_size = "11px"
    a2.xaxis.major_label_text_font_style = 'bold'
    a2.grid.grid_line_color=None
    a2.toolbar.autohide = True
    return a2

def Transactions():
    df = pd.read_csv('BokehApp/Data/HT_SalesAll.csv', delimiter='\t')
    df.reset_index(inplace=True)
    df = df[['Year','Dublin New', 'Ireland New','Dublin Existing','Ireland Existing']]
    df.set_index('Year', inplace=True)
    varpti = ['Dublin New', 'Ireland New', 'Dublin Existing','Ireland Existing']
    #the value of the y axis has to be in str format
    yearspti = '2010','2011','2012', '2013', '2014', '2015', '2016', '2017', '2018' #df3.index.values.tolist()
    xrange = df.values.max()*1.01
    sourcepti = ColumnDataSource(data=dict(x=yearspti, y=df['Dublin New'], y1=df['Ireland New'],y2=df['Dublin Existing'], y3=df['Ireland Existing']))
    pti = figure(y_range=yearspti, x_range=(0, xrange), plot_height=350, plot_width=550, title='Properties Transactions in Ireland', tools='pan, wheel_zoom, box_zoom, reset')
    pti.hbar(y=dodge('x', -0.2, range=pti.y_range), right='y', height=0.15, source=sourcepti, color='#440154', legend=value('Dublin New'))
    pti.hbar(y=dodge('x', 0, range=pti.y_range), right='y1', height=0.15, source=sourcepti, color='#30678D', legend=value('Ireland New'))
    pti.hbar(y=dodge('x', 0.2, range=pti.y_range), right='y2', height=0.15, source=sourcepti, color='#35B778', legend=value('Dublin Exsiting')) 
    pti.hbar(y=dodge('x', 0.4, range=pti.y_range), right='y3', height=0.15, source=sourcepti, color='#FDE724', legend=value('Ireland Exsiting')) 
    
    hoverpti = HoverTool()
    hoverpti.tooltips=[('Dubin New', '@y'), ('Ireland New', '@y1'), ('Dublin Existing', '@y2'), ('Ireland Existing', '@y3')]
    pti.add_tools(hoverpti)

    pti.legend.location='bottom_right'
    pti.y_range.range_padding = 0.02
    pti.grid.grid_line_color = None
    tick_labels_pti = {'10000':'10K','20000':'20K','30000':'30K','40000':'40K','50000':'50K'}
    pti.xaxis.major_label_overrides = tick_labels_pti
    pti.legend.background_fill_alpha=None
    pti.legend.border_line_alpha=0
    pti.legend.label_text_font_size = "11px"
    pti.legend.click_policy="hide"
    pti.title.text_font_size = '15px'
    #pti.axis.major_label_text_font_style = 'bold'
    pti.xaxis.major_label_text_font_style = 'bold'
    pti.toolbar.autohide = True
    return pti

def NewRegistered():
    dfnr = pd.read_csv('BokehApp/Data/NewRegHouses_CLEANED.csv', delimiter='\t', index_col='Year_RNH')
    xnr = '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'
    pnr = figure(x_range=xnr, plot_height=350, plot_width=550, title='Number of new properties registered', tools='pan, wheel_zoom, box_zoom, reset')
    sourcenr = ColumnDataSource(data= dict(x=xnr, y=dfnr['Ireland'], y1=dfnr['Dublin']))
    pnr.line(x='x', y='y', line_width=2.5, line_color='#440154', source=sourcenr, legend=value('Ireland'))
    pnr.line(x='x', y='y1', line_width=2.5, line_color='#FDE724', source=sourcenr, legend=value('Dublin'))
    pnr.circle(x='x', y='y', size=5, color='#B2DD2C', source=sourcenr, legend=value('Ireland'))
    pnr.circle(x='x', y='y1', size=5, color='#35B778', source=sourcenr, legend=value('Dublin'))

    hoverpnr = HoverTool()
    hoverpnr.tooltips=[('Ireland', '@y'), ('Dublin', '@y1')]
    pnr.add_tools(hoverpnr)

    pnr.legend.location='top_right'
    #pnr.y_range.range_padding = 0.02
    pnr.xgrid.grid_line_color = None
    tick_labels_pnr = {'10000':'10K','20000':'20K','30000':'30K','40000':'40K','50000':'50K', '60000':'60K'}
    pnr.yaxis.major_label_overrides = tick_labels_pnr
    #pnr.legend.background_fill_alpha=None
    pnr.legend.border_line_alpha=0
    pnr.legend.label_text_font_size = "11px"
    pnr.legend.click_policy="hide"
    pnr.title.text_font_size = '15px'
    #pti.axis.major_label_text_font_style = 'bold'
    pnr.xaxis.major_label_text_font_style = 'bold'
    pnr.toolbar.autohide = True
    return pnr

def nonOccupiers():
    #bokeh_doc = curdoc()
    dfn = pd.read_csv('BokehApp/Data/TT_nonOccupier.csv', delimiter='\t', index_col='Years')
    dfnt = dfn[['Total Transactions', 'Total Non-Occupiers']]
    rowX = '2010', '2011','2012','2013','2014','2015','2016', '2017', '2018'
    sourcent = ColumnDataSource(data=dict( x = rowX, y=dfnt['Total Transactions'], y1=dfnt['Total Non-Occupiers']))
    pn = figure(x_range=rowX, plot_height=350, plot_width=550, title='Properties Transactions in Ireland', y_axis_label=None, x_axis_label=None, tools = 'pan, wheel_zoom, box_zoom, reset')
    pn.vbar(x=dodge('x', 0.0, range=pn.x_range), top='y', width=0.3, source=sourcent, color='#440154', legend=value('Total Transactions'))
    pn.vbar(x=dodge('x', -0.35, range=pn.x_range), top='y1', width=0.3, source=sourcent, color='#FDE724', legend=value('Total Non-Occupiers'))
    
    pn.x_range.range_padding = 0.05
    pn.legend.location = 'top_left'
    hoverpn = HoverTool()
    hoverpn.tooltips=[('Transactions', 'total @y / non-occupiers @y1')]
    pn.add_tools(hoverpn)
    tick_labelspn = {'10000':'10K','20000':'20K','30000':'30K','40000':'40K','50000':'50K', '60000':'60K'}
    pn.yaxis.major_label_overrides = tick_labelspn
    pn.legend.background_fill_alpha=None
    pn.legend.border_line_alpha=0
    pn.legend.label_text_font_size = "11px"
    pn.y_range.end = dfnt.values.max()*1.1+1
    pn.legend.click_policy="hide"
    pn.title.text_font_size = '15px'
    pn.xaxis.major_label_text_font_style = 'bold'
    pn.grid.grid_line_color=None
    pn.toolbar.autohide = True
    #return pn
    #show(pn)def NonOccupiers(): 
    dfn1 = pd.read_csv('BokehApp/Data/TT_nonOccupier.csv', delimiter='\t', index_col='Years')
    dfn3 = dfn1[['Former Owner-Occupier', 'Non-Occupier', 'Non-Household Buyer']]
    rX = '2010', '2011','2012','2013','2014','2015','2016', '2017', '2018'

    srcn3 = ColumnDataSource(data=dict( x = rX,
                                    y=dfn3['Former Owner-Occupier'],
                                    y1=dfn3['Non-Occupier'],
                                    y2=dfn3['Non-Household Buyer']))
    pn3 = figure(x_range=rX, plot_height=350, plot_width=550, title='Properties Transactions in Ireland', y_axis_label=None, x_axis_label=None, tools = 'pan, wheel_zoom, box_zoom, reset')

    pn3.line(x='x', y='y', line_width=2.5, line_color='#440154', source=srcn3, legend=value('Former Owner-Occupier'))
    pn3.line(x='x', y='y1', line_width=2.5, line_color='#FDE724', source=srcn3, legend=value('Non-Occupier'))
    pn3.circle(x='x', y='y', size=5, color='#B2DD2C', source=srcn3, legend=value('Former Owner-Occupier'))
    pn3.circle(x='x', y='y1', size=5, color='#440154', source=srcn3, legend=value('Non-Occupier'))
    pn3.line(x='x', y='y2', line_width=2.5, line_color='#9DD93A', source=srcn3, legend=value('Non-Household Buyer'))
    pn3.circle(x='x', y='y2', size=5, color='#365A8C', source=srcn3, legend=value('Non-Household Buyer'))

            #pne.vbar(x='x', top='y', width=0.4, source=srcne, color='#440154', legend=value('Existing'))
            #pne.vbar(x='x', top='y1', width=0.4, source=srcne, color='#FDE724', legend=value('New'))

    pn3.legend.location = 'top_left'
    hoverpn3 = HoverTool()
    hoverpn3.tooltips=[('Former Owner', '@y'),('Non-Occupier', '@y1'), ('Non-Household', '@y2')]
    pn3.add_tools(hoverpn3)
    tick_labelspn3 = {'5000':'5K','10000':'10K','15000':'15K','20000':'20K','25000':'25K'}
    pn3.yaxis.major_label_overrides = tick_labelspn3
            #pn.xaxis.major_label_overrides = {'2010':'2010', '2011':'2011'}
    #pn3.legend.background_fill_alpha=None
    #pn3.legend.border_line_alpha=0
    pn3.legend.label_text_font_size = "11px"
            #pne.y_range.end = dfnt.values.max()*1.1+1
            #pn.x_range.start = rowX*1.1+1
    pn3.legend.click_policy="hide"
    pn3.title.text_font_size = '15px'
    pn3.xaxis.major_label_text_font_style = 'bold'
    pn3.xgrid.grid_line_color=None
    pn3.toolbar.autohide = True
    #return pn3
    #show(pn3)

    dfne = pd.read_csv('BokehApp/Data/HT_NewExisiting.csv', delimiter='\t', index_col='Years')
    rX = '2010', '2011','2012','2013','2014','2015','2016', '2017', '2018'

    srcne = ColumnDataSource(data=dict( x = rX,
                                    y=dfne['Existing'],
                                    y1=dfne['New']))
    pne = figure(x_range=rX, plot_height=350, plot_width=550, title='Properties Transactions in Ireland', y_axis_label=None, x_axis_label=None, tools = 'pan, wheel_zoom, box_zoom, reset')

    pne.line(x='x', y='y', line_width=2.5, line_color='#440154', source=srcne, legend=value('Existing'))
    pne.line(x='x', y='y1', line_width=2.5, line_color='#FDE724', source=srcne, legend=value('New'))
    pne.circle(x='x', y='y', size=5, color='#B2DD2C', source=srcne, legend=value('Existing'))
    pne.circle(x='x', y='y1', size=5, color='#35B778', source=srcne, legend=value('New'))

            #pne.vbar(x='x', top='y', width=0.4, source=srcne, color='#440154', legend=value('Existing'))
            #pne.vbar(x='x', top='y1', width=0.4, source=srcne, color='#FDE724', legend=value('New'))

    pne.legend.location = 'top_left'
    hoverpne = HoverTool()
    hoverpne.tooltips=[('Transactions', 'Exisiting @y / New @y1')]
    pne.add_tools(hoverpne)
    tick_labelspne = {'10000':'10K','20000':'20K','30000':'30K','40000':'40K'}
    pne.yaxis.major_label_overrides = tick_labelspne
            #pn.xaxis.major_label_overrides = {'2010':'2010', '2011':'2011'}
    pne.legend.background_fill_alpha=None
    pne.legend.border_line_alpha=0
    pne.legend.label_text_font_size = "11px"
            #pne.y_range.end = dfnt.values.max()*1.1+1
            #pn.x_range.start = rowX*1.1+1
    pne.legend.click_policy="hide"
    pne.title.text_font_size = '15px'
    pne.xaxis.major_label_text_font_style = 'bold'
    pne.xgrid.grid_line_color=None
    pne.toolbar.autohide = True
    #show(pne)

    dfn = pd.read_csv('BokehApp/Data/TT_nonOccupier.csv', delimiter='\t', index_col='Years')
    dfnt = dfn[['Total Transactions', 'Total Non-Occupiers']]

    rowX = '2010', '2011','2012','2013','2014','2015','2016', '2017', '2018'

    sourcent = ColumnDataSource(data=dict( x = rowX,
                                        y=dfnt['Total Transactions'],
                                        y1=dfnt['Total Non-Occupiers']))
    pn = figure(x_range=rowX, plot_height=350, plot_width=550, title='Properties Transactions in Ireland', y_axis_label=None, x_axis_label=None, tools = 'pan, wheel_zoom, box_zoom, reset')
        #pn.x_range=rowX
    pn.vbar(x=dodge('x', 0.0, range=pn.x_range), top='y', width=0.3, source=sourcent, color='#440154', legend=value('Total Transactions'))
    pn.vbar(x=dodge('x', -0.35, range=pn.x_range), top='y1', width=0.3, source=sourcent, color='#FDE724', legend=value('Total Non-Occupiers'))

        #pn.x_range.factors = xstr
        #x_range = FactorRange(factors=['2010', '2011', '2012','2013','2014','2015','2016','2017','2018'])
    pn.x_range.range_padding = 0.05
    pn.legend.location = 'top_left'
    hoverpn = HoverTool()
    hoverpn.tooltips=[('Transactions', 'total @y / non-occupiers @y1')]
    pn.add_tools(hoverpn)
    tick_labelspn = {'10000':'10K','20000':'20K','30000':'30K','40000':'40K','50000':'50K', '60000':'60K'}
    pn.yaxis.major_label_overrides = tick_labelspn
        #pn.xaxis.major_label_overrides = {'2010':'2010', '2011':'2011'}
    pn.legend.background_fill_alpha=None
    pn.legend.border_line_alpha=0
    pn.legend.label_text_font_size = "11px"
    pn.y_range.end = dfnt.values.max()*1.1+1
        #pn.x_range.start = rowX*1.1+1
    pn.legend.click_policy="hide"
    pn.title.text_font_size = '15px'
    pn.xaxis.major_label_text_font_style = 'bold'
    pn.grid.grid_line_color=None
    pn.toolbar.autohide = True
    #show(pn)
    t1 = Panel(child=pn, title='Overview')
    t2 = Panel(child=pne, title='Type of sale')
    t3 = Panel(child=pn3, title='Type of buyer')
    tabs = Tabs(tabs=[t1,t2,t3])
    return tabs
    #bokeh_doc.add_root(tabs)

    #show(tabs)






