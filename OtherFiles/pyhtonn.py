import sys
from io import BytesIO
import requests
from PIL import Image


# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:


def get_spn(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    x1, y1 = map(float, toponym['boundedBy']['Envelope']['upperCorner'].split(' '))
    x2, y2 = map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split(' '))
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    ll = ','.join([toponym_longitude, toponym_lattitude])
    spn = f'{abs(x2 - x1) / 2.0},{abs(y1 - y2) / 2.0}'
    return ll, spn


def get_map(place):
    ll, spn = get_spn(place)
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": "map",
        "pt": "{0},pm2dgl".format(ll)
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(
        response.content)).show()

    # Создадим картинку


if __name__ == '__main__':
    toponym_to_find = " ".join(sys.argv[1:])
    if not toponym_to_find:
        toponym_to_find = input('Введите объект для поиска: ')
    get_map(toponym_to_find)