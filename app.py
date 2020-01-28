from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
	name = request.args.get("name")
	if name == None:
		name = "Reinhold"
	return render_template("index.html", name=name)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
	#serve(app, host='0.0.0.0', port=8080)