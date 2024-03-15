import requests
import json

with open('A12.json', 'r') as file:
    data = json.load(file)

out = []

url = f"http://{data['server']}:{data['port']}/"
dishes = data['dishes']
response = requests.get(url)
json11 = response.json()

for k, value in json11.items():
    for i in dishes:
        if k in i.split() and (
                i.count('a') + i.count('e') + i.count('y') + i.count('u') + i.count('i') + i.count('o') == value):
            out.append(i)
a = sorted(out, reverse=True)
print('; '.join(a))
