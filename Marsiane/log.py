from data.users import User
from data.jobs import Jobs
import db
from data.db_session import global_init, create_session

global_init(input())
db_sess = create_session()
lens = 0
for elem in db_sess.query(User).filter(User.address == 'module_1', User.age >= 21):
    elem.address = 'module_3'
    db_sess.commit()
    db_sess.close()

# db/mars_explorer.db
