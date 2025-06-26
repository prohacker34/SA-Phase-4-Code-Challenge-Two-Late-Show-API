from flask import Flask, request, make_response
from flask_migrate import Migrate
from models import db, User,Episode,Guest,Appearance
from flask_sqlalchemy import SQLAlchemy

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

@app.route('/episodes/<int:episode_id>', methods=['GET','DELETE'])
def episode(id):
    episode=db.get_or_404(Episode,id)
    if request.method == 'GET':
        return make_response(Episode.to_dict(),200)

    if request.method == 'DELETE':
        db.session.delete(episode)
        db.session.commit()

        return make_response({'message': 'Episode deleted successfully'}, 204)


@app.route('/Appearances' , methods=['GET', 'POST'])
def post_appearances():

    if request.method == 'GET':
        appearances=[appearance.to_dict()for appearance in Appearance.query.all()]

        return make_response(appearances,200)
    if request.method == 'POST':
        data=request.get_json()

        new_appearance= Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(new_appearance)
        db.session.commit()

        return make_response(new_appearance.to_dict(), 201)



if __name__ == '__main__':
    app.run(debug=True)
