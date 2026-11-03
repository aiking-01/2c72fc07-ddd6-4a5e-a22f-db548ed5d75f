import csv
fname = 'data.csv'
fname_w = 'smalldata.csv'

with open(fname, encoding='CP932', newline="") as f:                # 読込み用のファイルを開く
    reader = csv.reader(f)                              # 読込み用のオブジェクトを作成
    for i in range(6):                                  # ヘッダー部の６行のうち、４行目の内容を変数 header に取り込む
        if i == 3:
            header = next(reader)
        else:
            next(reader)
    with open(fname_w, 'w', encoding='utf-8', newline="") as fw:    # 書込み用のファイルを開く … 書込みモード 'w' を忘れない
        # 以下の手順で data.csv の内容から必要なところを smalldata.csv に書き込む
        # (1) 書込み用のオブジェクトを作成
        # (2) ヘッダー部分を書込み
        # (3) 読み込むたびに、必要なデータを書き込む
        writer = csv.writer(fw)                                     # (1)
        writer.writerow([header[0], header[1], header[4]])          # (2)
        for row in reader:                                          # (3)
            writer.writerow([row[0], row[1], row[4]])

