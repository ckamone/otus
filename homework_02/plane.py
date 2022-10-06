"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight=1000, fuel=1000, fuel_consumption=1000, max_cargo=10000):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, kg):
        if kg + self.cargo <= self.max_cargo:
            self.cargo += kg
        else:
            raise CargoOverload(
                f'Невозможно загрузить вес {kg}. макс = {self.max_cargo}; текущая загрузка= {self.cargo}')

    def remove_all_cargo(self):
        temp = self.cargo
        self.cargo = 0
        return temp

    def __str__(self):
        return f'{Plane.__name__}: weight={self.weight}, fuel={self.fuel},' \
               f'consumption={self.fuel_consumption}, started={str(self.started)}'
