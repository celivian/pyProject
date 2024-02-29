from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("./db/mars_explorer.db")

job = Jobs()
job.team_leader = 1
job.job = '243rffer'
job.work_size = 2342
job.collaborators = '2'
job.is_finished = True
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()