class satiger:
    heigth = 170
    starvation = 100
    age = 2000

class tiger(satiger):
    age = 60
    horrible = 100

class kat(tiger):
    heigth = 30
    Bread = 60
    def __init__(self):
        print("Зріст",self.heigth)
        print("Голод" ,self.starvation)
        print("Рік" ,self.age)
        print("Лячність", self.horrible)
        print("Хліб", self.Bread)

ra = kat()