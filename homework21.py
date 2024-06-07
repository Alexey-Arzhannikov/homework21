class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def __init__(self):
        self.hp = 250

    def horse_powers(self):
        return f' {self.hp} л.с.'



class Nissan(Car, Vehicle):
    vehicle_type = "Седан"
    price = 1500000

    def horse_powers(self):
        print('Мощность: ', super().horse_powers(), '(турбонадув)')


GTR = Nissan()
GTR.horse_powers()
print('Тип кузова: ', GTR.vehicle_type)
print('Цена: ', GTR.price)
