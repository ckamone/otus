"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = None
    max_cargo = None

    def __init__(self, weight, fuel, fuel_consumption, max_cargo=1000):
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
