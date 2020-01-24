from flask import Flask, render_template, request, send_from_directory, json, make_response
import os
import sys
#test = sys.path.insert(0, '/py/')
from py import tweety
app = Flask(__name__)

#raw = tweety.get_tweets('realDonaldTrump',2)

posts=[
	{
		'author': 'lol',
		'handle': '@coop',
		'content': 'He had accidentally hacked into his companys server',
		'date_posted': 'January 1, 2020'
	}

]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('js', path)


@app.route('/update')
def updatecode():
    os.system('git pull origin master')
    return render_template('home.html', posts=posts) 

@app.route('/handle', methods = ['GET'])
def displaytweet():
	h = request.args.get('h')
	c = request.args.get('c')
	out = tweety.get_tweets(h, c)
	return(out), {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' ,port=1337)