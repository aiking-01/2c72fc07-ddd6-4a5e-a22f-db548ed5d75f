class Planet:
  def __init__(s,n,d,m,r):s.n,s.d,s.m,s.r=n,d,m,r
  def surface(s):return 4*3.14*s.d**2*s.r
  def print_planet(s):print(s.n,"\n太陽距離（億km）：",s.d,"\n直径（km）：",s.m,"\n質量（地球比）：",s.r)

# 動作の確認

venus = Planet("金星", 1.08, 12104, 0.815)
mars = Planet("火星", 2.28, 6792, 0.107)
venus.print_planet()
mars.print_planet()