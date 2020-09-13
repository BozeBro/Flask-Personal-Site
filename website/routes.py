from datetime import date
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_user, current_user, logout_user
from . import app, bcrypt
from .forms import LoginForm
from .models import Title, User

github = 'https://github.com/BozeBro'
year = date.today().strftime("%Y")
@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    posts = Title.query.all()
    return render_template(
        'home.html', 
        posts=posts,
        heading='Benedict\'s Website',
        subheading='Bringing you content by Yours Truly',
        image='home-bg.jpg',
        title='Benedict Ozua',
        year=year,
        github=github
    )

@app.route('/about')
def about():
    return render_template(
        'about.html', 
        heading='Resume', 
        subheading='This is what I do',
        image='notes-bg.png',
        title='Resume',
        github=github,
        year=year
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        heading='Contact Me',
        subheading='Have questions? I have answers.',
        image='gmail-bg.png',
        title='How to contact Me',
        github=github,
        year=year
    )

@app.route('/project')
def project():
    posts = Title.query.all()
    return render_template(
        'project.html',
        heading='My Projects',
        subheading='This is my Work',
        image='black-bg.jpg',
        github=github,
        posts=posts,
        title='Projects',
        year=year
        )
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # &$jLUM4B6Cg4WWf@
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            if user.permission == 'Admin':
                flash('You are logged in successfully!', 'success')
                return redirect('/admin')
            return redirect(url_for('home'))
    return render_template(
        'login.html',
        heading='Login Page',
        title='Login',
        github=github,
        form=form
        )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))