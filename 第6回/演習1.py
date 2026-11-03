fname = 'data.csv'
import csv
with open(fname, encoding='cp932', newline="") as f:
    a = csv.reader(f)
    next(a)
    next(a)
    next(a)
    print(next(a))
    next(a)
    next(a)
    while True:
        try:
            print(next(a))
        except Exception:
            break