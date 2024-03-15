import io
import logging
from json import dumps
from time import sleep

from flask import Flask
from multiprocessing import Process
from contextlib import contextmanager, redirect_stdout

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {
            'pie': [140, 223, 130, 111, 74, 229, 48],
            'donut': [152, 131, 287, 289, 121],
            'cake': [43, 51, 108, 65],
            'waffle': [117, 274, 262, 198, 198, 4]
        },
        {
            'crumpet': [164, 202, 56],
            'bagel': [27, 247, 59, 273, 174, 232],
            'donut': [279, 104, 262],
            'pretzel': [81, 21, 152, 111],
            'pie': [183, 169, 277, 213, 147, 137]
        }
    ]

    index = 0
    while (index := int(input('Введите номер примера: '))) not in (1, 2):
        ...
    server = Server('127.0.0.1', 5000, data[index - 1])
    with server.run():
        while (row := input('Введите "stop" для завершения работы сервера: ')) != 'stop':
            ...
