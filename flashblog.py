from flask import Flask, render_template, url_for
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

@app.route('/update')
def updatecode():
    os.system('git pull origin master')
    return render_template('home.html')    



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' ,port=1337)
