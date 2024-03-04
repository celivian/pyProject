from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("./db/mars_explorer.db")

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.hashed_password = '12345'
user.setPassword(user.hashed_password)
user.email = "scott_chief@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Bro"
user.name = "Borov"
user.age = 39
user.position = "bothman"
user.speciality = "teacher"
user.address = "nose"
user.hashed_password = '1234'
user.setPassword(user.hashed_password)
user.email = "borov22@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Max"
user.name = "Maxbetov"
user.age = 19
user.position = "cook"
user.speciality = "boatswain"
user.address = "tail"
user.hashed_password = '123456'
user.setPassword(user.hashed_password)
user.email = "maxes31@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Tom"
user.name = "Haaland"
user.age = 18
user.position = "pilot"
user.speciality = "flyer"
user.address = "wing"
user.hashed_password = '123'
user.setPassword(user.hashed_password)
user.email = "haaland1@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()
