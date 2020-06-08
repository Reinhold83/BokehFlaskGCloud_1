from flask import Flask, render_template, request
from bokeh.embed import components
from plots1 import houseStockPlot, vacantPlot, Transactions, NewRegistered, nonOccupiers, pie_chart
from flask_bootstrap import Bootstrap

app = Flask(__name__)
#app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = 'oratoroeuaroupadoreideroma123'
#app.static_folder = 'static'
Bootstrap(app)
#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/bokeh')
def bokeh():
    script, div = components(houseStockPlot())
    script1, div1 = components(vacantPlot())
    script2, div2 = components(Transactions())
    script3, div3 = components(NewRegistered())
    script4, div4 = components(nonOccupiers())
    script5, div5 = components(pie_chart())


    return render_template('bokeh.html', script=script, div=div, script1=script1,
    div1=div1, script2=script2, div2=div2, script3= script3, div3=div3, script4=script4, div4=div4,
    script5=script5, div5=div5)