from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/")
@app.route("/index")
def index():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("jobs.html", jobs=jobs)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')