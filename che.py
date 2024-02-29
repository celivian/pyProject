global_init(input())
db_sess = create_session()
a = User.address
b = User.speciality
c = User.position

for id in db_sess.query(User).filter(a == 'module_1', 'engineer' not in b, 'engineer' not in c).all():
    print(user)
