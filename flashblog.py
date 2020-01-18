from flask import Flask, render_template, request, send_from_directory, json, make_response
import os
app = Flask(__name__)

posts=[
	{
		'author': 'Cooper Wallace',
		'content': 'content',
		'date_posted': 'January 1, 2020'
	},
	{
		'author': 'Sam Wallace',
		'content': 'content',
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


@app.route('/update')
def updatecode():
    os.system('git pull origin master')
    return render_template('home.html', posts=posts) 

@app.route('/handle', methods = ['GET','POST'])
def displaytweet():
	handle = request.args.get('handle')
	print(handle)
	return render_template('handle.html', handle = handle)
	


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' ,port=1337)
