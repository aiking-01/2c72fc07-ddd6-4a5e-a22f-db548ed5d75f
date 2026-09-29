d = 12     # 直径
a = 10     # １辺の長さ

r = d / 2
PI = 3.14159
ball = r**3*4/3*PI # 球の体積の計算
dice = a**3 # 立方体の体積の計算

# 球および立方体の面積を表示
print(f"直径 {d}cm の球の体積：", ball)
print(f"１辺 {a}cm の立方体の体積：", dice)

# 体積の大小を比較して結果を表示
if ball > dice:
    print(f"直径 {d}cm の球のほうが、１辺 {a}cm の立方体よりも 体積が大きい")
elif dice > ball:
    print(f"直径 {d}cm の球よりも、１辺 {a}cm の立方体のほうが 体積が大きい")
else:
    print(f"直径 {d}cm の球よりと、１辺 {a}cm の立方体の体積は等しい。")
