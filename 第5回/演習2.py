# sample2.py

text = ""
try:
    with open("data.txt", "r") as f:
        text = f.read()
except FileNotFoundError:
    print("ファイルが見つかりません。")
except UnicodeDecodeError:
    print("ファイルのエンコーディングが正しくありません。")

print(text)