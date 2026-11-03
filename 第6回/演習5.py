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
