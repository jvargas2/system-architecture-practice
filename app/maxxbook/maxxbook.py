from flask import request, session, g, redirect, url_for, abort, render_template, flash
from maxxbook.index import app, db
from maxxbook.models import User
from maxxbook.models import Post

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def show_posts():
	posts = Post.query.all()
	return render_template('show_posts.html', posts=posts)

@app.route('/add', methods=['POST'])
def add_post():
	if not session.get('logged_in'):
		abort(401)

	new_post = Post(request.form['title'], request.form['body'])
	db.session.add(new_post)
	db.session.commit()

	flash('New entry was successfully posted')

	return redirect(url_for('show_posts'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_posts'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_posts'))

if __name__ == "__main__":
	app.run()
