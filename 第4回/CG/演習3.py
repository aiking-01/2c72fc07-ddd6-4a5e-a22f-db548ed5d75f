with open("Sample_utf8.txt","w",encoding="utf-8")as d:
    with open("sample.txt","r",encoding="shift-jis")as f:d.write(f.read())