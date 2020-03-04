from application import db

from application import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(500), nullable=False, unique=True)
	password = db.Column(db.String(500), nullable=False)
	def __repr__(self):
		return ''.join([
		'UserID: ', str(self.id),'\r\n', 'Email: ', self.email])


