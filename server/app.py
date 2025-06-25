from flask import Flask, request, make_response
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:cold123@localhost/late_show_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Welcome to the Late Show API!'

@app.route('/users', methods=['POST'])
def post():
    data = request.get_json()
    new_user = User(username=data['username'], password_hash=data['password_hash'])
    db.session.add(new_user)
    db.session.commit()
    return make_response(new_user.to_dict(), 201)  

if __name__ == '__main__':
    app.run(debug=True)
