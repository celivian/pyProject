global_init(input())
db_sess = create_session()

for elem in db_sess.query(User).filter((User.position.like('%chef%')) | (User.position.like('%middle%'))):
    print(f'{elem} {elem.position} {elem.speciality}')
