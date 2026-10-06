# 関数型プログラミング　（データを関数で変換していくことに着目したプログラミング）


# 関数の定義
def subtotal(price, number):     # 単価 と 数量 から 小計 を計算
    return int(price * number)

def calc_tax(amount, rate):           # 税抜き金額 と 税率 から 消費税 を計算
    return int(amount * rate)

def add_tax(amount, rate):       # 税抜き金額 と 税率 から 税込み金額 を計算
    return int(amount + calc_tax(amount, rate))

# 与えられた値（各商品の単価、各商品の数量）
bento, sandwich, drink = 500, 300, 100
bento_num, sandwich_num, drink_num = 1, 2, 1

# #（コード作成）# 合計金額 total を計算
bentoprice = subtotal(bento,bento_num)
sandwichprice = subtotal(sandwich,sandwich_num)
drinkprice = subtotal(drink,drink_num)
total = bentoprice + sandwichprice + drinkprice

# #（コード作成）# 合計金額 total に対する消費税 tax を計算し、支払金額 payment を求める
tax = calc_tax(total,0.08)
payment = add_tax(total,0.08)

# 金額の表示
print("合計金額：", total, "円")
print("消費税：", tax, "円")          # 第１回講義の演習７での出題では 関数 tax() と 変数 tax が登場しました。異なる名前を使うべきでした。
print("支払金額：", payment, "円")