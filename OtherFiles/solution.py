from flask import Flask, url_for

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
                    <img src="{url_for('static', filename='img/MARS.png')}"/>
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


@app.route('/astronaut_selection')
def austro():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                     integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                      crossorigin="anonymous">
                    <link rel="stylesheet" href="static/css/style.css"
                  </head>
                  <body>
                    <p class="h1">Анкета претендента</p>
                    <p class="h2">на участие в миссии</p>
                    <div class="row">
                      <div class="col-sm">
                        <form>
                          <input type="text" id="surname" placeholder="Введите фамилию">
                          <input type="text" id="name" placeholder="Введите имя">
                          <input type="text" id="email" placeholder="Введите адрес почты">
                          <p>Какое у Вас образование?</p>
                          <select>
                            <option>Начальное</option>
                            <option>Основное</option>
                            <option>Среднее общее</option>
                            <option>Среднее профессиональное</option>
                            <option>Высшее</option>
                          </select>
                          <p>Какие у Вас профессии?</p>
                          <label>
                            <input type="checkbox" class="check">
                            Инженер-исследователь
                          </label>
                        <form/>
                      </div>
                    </div>
                  </body>
                </html>"""


@app.route('/ur')
def urok():
    return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
          crossorigin="anonymous">
    <title>{{title}}</title>
</head>
<body>
<header>
    <nav class="navbar navbar-light bg-light">
        <a class="navbar-brand" href="#">Наше приложение</a>
    </nav>
</header>
<!-- Begin page content -->
<main role="main" class="container">
    {% block content %}{% endblock %}
</main>
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
