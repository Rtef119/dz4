class satiger:
    heigth = 170
    starvation = 100
    age = 2000

class tiger(satiger):
    age = 60

class kat(tiger):
    heigth = 30
    def __init__(self):
        print("Зріст",self.heigth)
        print("Голод" ,self.starvation)
        print("Рік" ,self.age)

ra = kat()