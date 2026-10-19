import os
os.system("powershell -Command date > datetest.txt")
for i in range(3):os.system("powershell -Command date >> datetest.txt")
with open("convert2.py","w") as p:
    p.write("""with open("datetest_utf8.txt","w",encoding="utf-8")as d:
    with open("datetest.txt","r")as f:
        d.write(f.read())""")
import convert2
os.system("powershell -Command dir")