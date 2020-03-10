from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Register')


    def validate_email(self,email):

        users=User.query.filter_by(email=email.data).first()

        if users:
          raise ValidationError("Email already in use")


class GenerateForm(FlaskForm):

	goalkeeper = StringField('Goalkeeper',
		validators=[
			DataRequired(),
			Length(min=2, max=100)
        	]
    	)


	defender = StringField('Defender',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)


	midfielder = StringField('Midfielder',
		validators = [
			DataRequired(),
			Length(min=2, max=100)
        	]
	)


	forward = StringField('Forward',
		validators = [
			DataRequired(),
			Length(min=2, max=1000)
		]
	 )
	submit = SubmitField('Generate')
