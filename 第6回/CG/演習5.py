import csv,requests

def get_lonlat(address):
    # 国土地理院の住所検索API
    url = f"https://msearch.gsi.go.jp/address-search/AddressSearch?q={address}"

    response = requests.get(url)
    data = response.json()

    if data:
        # 返却される座標は [経度, 緯度] の順
        lon, lat = data[0]["geometry"]["coordinates"]
    else:
        lon, lat = -1, -1

    return (lon, lat)

with open("schools.csv",encoding='utf-8-sig',newline="") as f,open("univ.csv",'w',encoding='utf-8',newline="") as g:w=csv.writer(g);w.writerow(['名称','住所','longitude','latitude']);w.writerows([r[5],r[6],*get_lonlat(r[6])]for r in csv.reader(f)if r and r[0][:1]=='F'and'大阪府'in r[6])
