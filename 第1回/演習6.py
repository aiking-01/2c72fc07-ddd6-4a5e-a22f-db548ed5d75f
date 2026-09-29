# 手続き型プログラミング（何を、どの順番で処理するか に着目してプログラムを構成）

bento, sandwich, drink = 500, 300, 100
bento_num, sandwich_num, drink_num = 1, 2, 1

##### ここにプログラムを作成して、「金額の表示」につなげること

total = bento*bento_num+sandwich*sandwich_num+drink*drink_num
tax = total * 0.08
payment = total + tax
# 金額の表示
print("合計金額：", total, "円")
print("消費税：", tax, "円")
print("支払金額：", payment, "円")