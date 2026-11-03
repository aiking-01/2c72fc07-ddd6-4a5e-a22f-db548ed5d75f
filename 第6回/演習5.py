import csv
import requests

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

fname = "schools.csv"        # 入力ファイル
fname_w = "univ.csv"         # 作成するファイル

with open(fname, encoding='utf-8-sig', newline="") as f:
    reader = csv.reader(f)
    with open(fname_w, 'w', encoding='utf-8', newline="") as fw:
        writer = csv.writer(fw)
        writer.writerow(['名称', '住所', 'longitude', 'latitude'])
        for row in reader:
            if row and row[0][:1] == 'F':
                name = row[5]
                address = row[6]
                if '大阪府' in address:
                    lon, lat = get_lonlat(address)
                    writer.writerow([name, address, lon, lat])
