with open("sample.txt", "r", encoding="shift-jis") as f:
    code = f.read()
with open("Sample_utf8.txt", "w", encoding="utf-8") as d:
    d.write(code)