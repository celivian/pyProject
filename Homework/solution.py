from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    sp = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
          'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    print('</br>'.join(sp))
    return '</br>'.join(sp)


@app.route('/image_mars')
def image():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/img/MARS.png"/>
                    <p>Вот она какая, красная планета!</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <title>Колонизация</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                     integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                      crossorigin="anonymous">
                    <link rel="stylesheet" href="static/css/style.css"
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/MARS.png"/>
                    <div id="css1" class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div id="css2"class="alert alert-primary" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div id="css3" class="alert alert-primary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div id="css4" class="alert alert-primary" role="alert">
                      И начнем с Марса!
                    </div>
                    <div id="css5" class="alert alert-primary" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                          <div class="lol">
                            <h1>Анкета претендента</h1>
                            <h2>на участии в миссии</h2>
                          </div>
                            
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label id="label" for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <label id="label" for="checks">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check" id="checks">
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="acceptRules1" name="work1">
                                        <label class="form-check-label" for="acceptRules1">Инженер-исследователь</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="acceptRules2" name="work2">
                                        <label class="form-check-label" for="acceptRules2">Инженер-строитель</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="acceptRules3" name="work3">
                                        <label class="form-check-label" for="acceptRules3">Пилот</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="acceptRules4" name="work4">
                                        <label class="form-check-label" for="acceptRules4">Метеоролог</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="acceptRules5" name="work5">
                                        <label class="form-check-label" for="acceptRules5">Инженер по жизнеобеспечению</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="acceptRules6" name="work6">
                                        <label class="form-check-label" for="acceptRules6">Инженер по радиационной защите</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="acceptRules7" name="work7">
                                        <label class="form-check-label" for="acceptRules7">Врач</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="acceptRules8" name="work8">
                                        <label class="form-check-label" for="acceptRules8">Экзобиолог</label>
                                    </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">ОТправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        for i in list(request.form):
            print(i, '=', request.form[i])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
