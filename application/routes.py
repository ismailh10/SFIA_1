from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt
from application.models import Bookings, Users
from application.forms import BookingForm, RegistrationForm, LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Users.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=login_form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	register_form = RegistrationForm()
	if register_form.validate_on_submit():
		new_user = Users(email=register_form.email.data, password=bcrypt.generate_password_hash(register_form.password.data))
		db.session.add(new_user)
		db.session.commit()
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=register_form)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/about')
def about():
	return render_template('about.html', title='About')


@app.route('/booking/search', methods=['GET', 'POST'])
def booking():
	form = BookingForm()
	if form.validate_on_submit():
		booking = BookingForm(
		first_name = form.first_name.data,
                last_name = form.last_name.data,
                location = form.location.data,
		booking_type = form.booking_type.data,
		)

		db.session.add(booking)
		db.session.commit()

		return redirect(url_for('booking/available'))
	return render_template('booking.html',form=form)



