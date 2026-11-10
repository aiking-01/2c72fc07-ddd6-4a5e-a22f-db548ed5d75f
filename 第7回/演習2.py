fname = 'planets.csv'
with open(fname, 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    n=next(reader)  # ヘッダー行を読み飛ばす
    MX=float(n[2])/float(n[3])
    try:
        while True:
            n=next(reader)
            V=float(n[2])/float(n[3])
            if MX<V:
                MX=V
                name=n[0]
    except StopIteration:
        print(name)
