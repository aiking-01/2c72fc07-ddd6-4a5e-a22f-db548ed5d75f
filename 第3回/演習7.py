# Planetクラスの作成

class Planet:
  def __init__(self,name,distance,diameter,massratio):
    self.name=name
    self.distance=distance
    self.diameter=diameter
    self.massratio=massratio
  def surface(self):
    return 4*3.14*self.distance**2*self.massratio
  def print_planet(self):
    print(self.name)
    print("　太陽距離（億km）：",self.distance)
    print("　直径（km）：",self.diameter)
    print("　質量（地球比）：",self.massratio)

# 動作の確認

venus = Planet("金星", 1.08, 12104, 0.815)
mars = Planet("火星", 2.28, 6792, 0.107)
venus.print_planet()
mars.print_planet()