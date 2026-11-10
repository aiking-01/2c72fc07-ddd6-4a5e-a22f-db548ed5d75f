import csv

header = ["惑星名", "英語名", "直径(km)", "太陽からの平均距離(億km)"]

jname = ["水星", "金星", "地球", "火星", "木星", "土星", "天王星", "海王星"]
ename = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
diameter = [4879, 12104, 12742, 6779, 139820, 116460, 50724, 49244]
distance = [0.58, 1.08, 1.50, 2.28, 7.79, 14.3, 28.7, 45.0]

# 以下に csv ファイルを作成する部分を入力すること。
with open("planets.csv", "w", newline="", encoding="utf-8") as f:
    print(*header, sep=",", file=f)
    for a, b, c, d in zip(jname, ename, diameter, distance):
        print(a, b, c, d, sep=",", file=f)