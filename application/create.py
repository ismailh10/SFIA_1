from application import db
from application.models import Posts

db.drop_all()
db.create_all()

python3 create.py




from application import Posts

@app.route('/')
@app.route('/home')
def home():
    postData = Posts.query.all()
    return render_template('home.html', title='Home', posts=postData)

