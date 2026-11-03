import csv
MAX=-99
with open('data.csv',encoding='cp932',newline="") as f:
    for row in list(csv.reader(f))[6:]:
        if float(row[1])>MAX:
            MAX=float(row[1])
    print(MAX)