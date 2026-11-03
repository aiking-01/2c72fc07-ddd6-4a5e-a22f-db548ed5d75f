fname = 'data.csv'
import csv
with open(fname, encoding='cp932', newline="") as f:
    fread = csv.reader(f)
    next(fread)
    next(fread)
    next(fread)
    temp = next(fread)
    next(fread)
    next(fread)
    while True:
        try:
            temp = next(fread)
            print(temp[0], temp[1], temp[4], temp[7], temp[11], temp[14], temp[17])
        except Exception:
            break