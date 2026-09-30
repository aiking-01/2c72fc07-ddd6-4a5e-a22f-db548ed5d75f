# 関数型プログラミング　（データを関数で変換していくことに着目したプログラミング）
# 関数の定義 ========================
def subtotal(price, number):     # 単価 と 数量 から 小計 を計算
    return price * number
def tax(amount, rate):           # 税抜き金額 と 税率 から 消費税 を計算
    return amount * rate
def add_tax(amount, rate):       # 税抜き金額 と 税率 から 税込み金額 を計算
    return amount + tax(amount, rate)
# ここまでが関数定義の部分 ==========
a,b,c=bento, sandwich, drink = 500, 300, 100
d,e,f=bento_num, sandwich_num, drink_num = 1, 2, 1
##### ここにプログラムを作成して、「金額の表示」につなげること
# 金額の表示
print("合計金額：", (t:=(g:=subtotal)(a,d)+g(b,e)+g(c,f)), "円")
print("消費税：", tax(t,0.08), "円")
print("支払金額：", add_tax(t,0.08), "円")