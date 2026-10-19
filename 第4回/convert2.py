with open("datetest_utf8.txt","w",encoding="utf-8")as d:
    with open("datetest.txt","r")as f:
        d.write(f.read())