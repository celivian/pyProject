import argparse
import requests
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument("host", metavar='host', type=str)
parser.add_argument("port", metavar='port', type=str)
parser.add_argument("vip", metavar="vip", type=str, nargs='*')
parser.add_argument("--unmult", metavar='unmult', type=int, default=7)
parser.add_argument("--mult", metavar='mult', type=int)
args = parser.parse_args()

dct = []

url = f"http://{args.host}:{args.port}/"
response = requests.get(url)
json11 = response.json()

for key, value in json11.items():
    if '--unmult' in sys.argv:
        sp = []
        c = 0
        for i in value:
            if i % args.unmult != 0:
                sp.append((i // args.unmult) * args.unmult)
            else:
                sp.append(i)
        dst = dict()
        dst['bakery'] = key
        dst['summary'] = sum(sp)
        for j in sp:
            if j % 2 == 0 and dst['summary'] % 2 == 0:
                c += 1
            elif j % 2 != 0 and dst['summary'] % 2 != 0:
                c += 1
        dst['number'] = c
        dct.append(dst)
    elif '--mult' in sys.argv:
        sp = []
        c = 0
        for i in value:
            if i % args.mult == 0:
                s = 0
                for j in str(i):
                    s += int(j)
                sp.append(s)
            else:
                sp.append(i)
        dst = dict()
        dst['bakery'] = key
        dst['summary'] = sum(sp)
        for j in sp:
            if j % 2 == 0 and dst['summary'] % 2 == 0:
                c += 1
            elif j % 2 != 0 and dst['summary'] % 2 != 0:
                c += 1
        dst['number'] = c
        dct.append(dst)
print(dct)

#
#
# print(json11)
#
#
# print(args)
