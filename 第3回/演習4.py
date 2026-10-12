class Prefecture:

    def __init__(self, name, population, area, capital, flower):
        self.name = name
        self.population = population
        self.area = area
        self.capital = capital
        self.flower = flower

# データを表示するメソッド
    def show(self):
        print("府県名：", self.name)
        print("人口：", self.population)
        print("面積：", self.area)
        print("府県庁所在地：", self.capital)
        print("府県の花：", self.flower)

# ここに、人口密度を計算するメソッドを追加
    def density(self):
        return self.population / self.area

