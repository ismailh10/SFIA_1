from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt
from application.models import  User
from application.forms import RegistrationForm, LoginForm, GenerateForm

@app.route('/')
@app.route('/home')
def home():
        return render_template('home.html', title='Home')

@app.route('/register', methods=['POST', 'GET'])
def register():
        form = RegistrationForm()
        if form.validate_on_submit():
                email=form.email.data
                password=bcrypt.generate_password_hash(form.password.data)
                users = User(email = email, password =password)
                db.session.add(users)
                db.session.commit()
                return redirect(url_for('login'))
        return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('generate'))
    return render_template('home.html', form=login_form)

@app.route('/generate', methods=['POST', 'GET'])
def generate():
	generate_form = GenerateForm()
	return render_template('generate.html', title='Generate', form=generate_form)

@app.route('/logout')
def logout():
        return render_template('logout.html', title='Logout')

