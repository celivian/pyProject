# Импорт библиотеки
import sqlite3

def arrival(data, sort=False):

    con = sqlite3.connect("duties.db")
    # Создание курсора
    cur = con.cursor()

    sent = f'SELECT id, city, ratio from Cities WHERE city in {tuple(data)}'
    result = cur.execute(sent).fetchall()
    indexs = []
    ratios = []
    for i in result:
        indexs.append(i[0])
    for i in result:
        ratios.append(i[2])
    sent2 = f'SELECT city_id, name, reason_id from People WHERE city_id in {tuple(indexs)}'
    result2 = cur.execute(sent2).fetchall()
    indexsreason = []
    for i in result2:
        indexsreason.append(i[2])
    sent1 = f'SELECT id, fee from Fees WHERE id in {tuple(indexsreason)}'
    result1 = cur.execute(sent1).fetchall()
    print(result)
    print(result2)
    print(result1)
    print(ratios)

    con.close()


data = ['Paris', 'Iconion', 'Baghdad', 'Nowhere', 'Qom']
arrival(data, sort=True)