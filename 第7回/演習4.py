import requests

url = "https://www.mext.go.jp/content/20260825-mxt_chousa01-000011635_6.csv"
response = requests.get(url)
response.encoding = response.apparent_encoding
"""def Nx(L):
    for i in L:yield i"""
fname = "schools.csv"
text = response.text.splitlines()
with open(fname, 'w', encoding='utf-8') as f:
    for i in text:
        if i[0] == 'F':
            f.write(",".join(i.split(",")[5:7]) + "\n")