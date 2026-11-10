fname = 'planets.csv'
fname_w = 'planets_s.csv'

with open(fname, 'r', encoding='utf-8', newline='') as fin,open(fname_w, 'w', encoding='utf-8', newline='') as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    next(reader)  # ヘッダー行を読み飛ばす
    for row in reader:
        del row[1]  # 英語名を削除
        writer.writerow(row[0:2])