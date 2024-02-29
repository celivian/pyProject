from flask import Flask
import random

app = Flask(__name__)


@app.route('/<swe>')

def index(swe):
    print(swe)
    answer = {'check': ''.join([chr(random.randint(65, 91)) for i in range(random.randint(0, 16))])}
   # with open('data3.json', 'r', encoding='utf-8') as stream:
    #    return stream.read()
    return 'ok'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)