from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

accounts = {"samar": "qwerty", "siwarha": "123", "hesham": "5645"}
facebook_friends=["Lilly","Maya","Leen", "Adam", "Fouad", "Gi"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		name = request.form['username'].casefold()
		pas = request.form['password']

		if name in accounts.keys() and pas == accounts[name]:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

	else:
		return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html',ff = facebook_friends)

@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	return render_template('friend_exists.html', n= name , ff = facebook_friends)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
