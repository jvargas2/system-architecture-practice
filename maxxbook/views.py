from flask import request, session, redirect, url_for, abort, render_template, flash
from maxxbook import app, db
from maxxbook.models import Post
from maxxbook.models import User


def current_user():
    if session.get('user'):
        user = User.query.filter_by(email=session['user']).first()
        return user
    else:
        return None


@app.route('/')
def show_posts():
    posts = Post.query.order_by(Post.pub_date.desc())
    users = User.query.all()
    users_by_id = {}
    post_titles = {}
    for user in users:
        users_by_id[user.id] = user
    if session.get('user'):
        user = current_user()
        return render_template('show_posts.html', user=user, posts=posts, users_by_id=users_by_id)
    else:
        return render_template('show_posts.html', user=None, posts=posts, users_by_id=users_by_id)


@app.route('/add', methods=['POST'])
def add_post():
    if session.get('user'):
        user = current_user()

        new_post = Post(user.id, request.form['body'])
        db.session.add(new_post)
        db.session.commit()

        flash('New entry was successfully posted')

        return redirect(url_for('show_posts'))

    else:
        abort(401)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user is None:
            error = 'Invalid email'
        elif request.form['password'] != user.password:
            error = 'Invalid password'
        else:
            session['user'] = user.email
            flash('You were logged in')
            return redirect(url_for('show_posts'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        new_user = User(email, first_name, last_name, password)
        db.session.add(new_user)
        db.session.commit()
        session['user'] = new_user.email
        flash('New user was successfully created')
        return redirect(url_for('show_posts'))
    return render_template('register.html', error=error)


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You were logged out')
    return redirect(url_for('show_posts'))


@app.route('/user/<int:user_id>')
def show_user_profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    name = user.first_name + ' ' + user.last_name
    return 'User %s' % name


@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return 'Post %s' % post.body
