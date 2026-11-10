import requests

url = "https://www.mext.go.jp/content/20260825-mxt_chousa01-000011635_6.csv"
response = requests.get(url)
response.encoding = response.apparent_encoding
text = response.text.splitlines()
fname_w = "univ.csv"
with open(fname_w, 'w', encoding='utf-8') as f:
    f.write("大学名,住所,緯度,経度\n")
    for i in text:
        if i[0] == 'F':
            textlist = i.split(",")
            if '大阪府' in textlist[6]:
                con=textlist[5:7]+list(get_lonlat(textlist[6]))
                print(*con,sep=",",file=f,end="\n")