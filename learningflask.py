from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash ## Importing flask and other needed stuff
app = Flask(__name__)## creating and preparing flask

@app.route("/") ## this creating a blank url, means if nothing in the url run the following function
def index():## this function will be called when url is blank
	return render_template('index.html') ## this tells flask to load the html code in index.html

@app.route("/hello/")## creating the url /hello/ for that will run the following function
@app.route("/hello/<name>")## creating the url /hello/<name> where name is a variable
@app.route("/hello/", methods=['POST']) ## this is another URL for this function that accepts a form with method POST
def hello(name=None):## this is the function that will be called, notice it takes an input, and it should be the same name of the one in the url, and the default value is None, other wise the value of it will be what is written in the url
	if ('name' in request.form.keys()):## this checks if we used the form, by checking if name input in the form
		name = request.form['name'] ## in case the form used, then this is how we get the value that is written in the form
	return render_template('hello.html', name=name)## here telling flask to load the html code in hello.html with the variable name

## to create more urls and functions simple create them the same way created above just change what you need

if __name__ == "__main__": ## this if statement is telling python when running this file run the following lines
	app.debug = True ## this to let flask show us errors if there is any
	app.run() ## this tells python to run flask
