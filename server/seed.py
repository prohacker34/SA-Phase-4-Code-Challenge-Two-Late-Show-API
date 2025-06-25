from models import User, Episode, Guest, Appearance
from app import db, app

with app.app_context():
    db.session.query(User).delete()
    db.session.query(Episode).delete()
    db.session.query(Guest).delete()
    db.session.query(Appearance).delete()

    Users=[]

    Alex=User(username='Alex', password_hash='password123')
    Jamie=User(username='Jamie', password_hash='password456')
    Taylor=User(username='Taylor', password_hash='password789')
    Jordan=User(username='Jordan', password_hash='password101112')

    Users.append(Alex)
    Users.append(Jamie)
    Users.append(Taylor)
    Users.append(Jordan)

    db.session.add_all([Alex, Jamie, Taylor, Jordan])
    db.session.commit()


    episodes= []

    episode1 = Episode(date='2023-01-01', number=1)
    episode2 = Episode(date='2023-01-08', number=2)
    episode3 = Episode(date='2023-01-15', number=3)
    episode4 = Episode(date='2023-01-22', number=4)

    episodes.append(episode1)
    episodes.append(episode2)
    episodes.append(episode3)
    episodes.append(episode4)

    db.session.add_all(episodes)
    db.session.commit()

    guests = []

    guest1 = Guest(name='John Doe', occupation='Actor')
    guest2 = Guest(name='Jane Smith', occupation='Musician')
    guest3 = Guest(name='Alice Johnson', occupation='Comedian')
    guest4 = Guest(name='Bob Brown', occupation='Author')

    guests.append(guest1)
    guests.append(guest2)
    guests.append(guest3)
    guests.append(guest4)

    db.session.add_all(guests)
    db.session.commit()

    appearances = []

    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)
    appearance3 = Appearance(rating=3, guest_id=guest3.id, episode_id=episode3.id)
    appearance4 = Appearance(rating=2, guest_id=guest4.id, episode_id=episode4.id)

    appearances.append(appearance1)
    appearances.append(appearance2)
    appearances.append(appearance3)
    appearances.append(appearance4)

    db.session.add_all(appearances)
    db.session.commit()