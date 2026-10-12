# 画面をリセット
tc.initializeTurtle()      # tc はモジュールで、その中の関数 initializeTurtle() を呼び出す

# ◎ タートルオブジェクトを作成（赤い線を描く亀、青い線を描く亀、緑の線を描く亀を、それぞれ別のオブジェクトとして作成）
turtle1 = tc.Turtle()      # tcモジュール の Turtleクラス のインスタンスを生成
turtle2 = tc.Turtle()
turtle3 = tc.Turtle()


# ◎３つのオブジェクトに対して色と速度を設定
turtle1.color('red')
turtle1.speed(5)

turtle2.color('blue')
turtle2.speed(10)
turtle3.color('green')
turtle3.speed(100)

# --- 矢印1（赤）の動き：四角形を描く（turtle1オブジェクト） ---
for i in range(4):
    turtle1.forward(80)
    turtle1.right(90)

# --- 矢印2（青）の動き：左上に向かって三角形を描く（turtle2オブジェクト） ---
turtle2.left(120)  # 最初に向きを変える
for i in range(3):
    turtle2.forward(100)
    turtle2.left(120)

# ◎--- 矢印3（緑）の動き：正六角形を描く（turtle3オブジェクト） ---

for i in range(6):
    turtle3.forward(100)
    turtle3.right(60)