"""
создайте класс `Plane`, наследник `Vehicle`
"""
from exceptions import CargoOverload
from engine import Vehicle

class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self, kg):
        if kg + self.cargo <= self.max_cargo:
            self.cargo += kg
        else:
            raise CargoOverload(f'Невозможно загрузить вес {kg}. макс = {self.max_cargo}; текущая загрузка= {self.cargo}')

    def remove_all_cargo(self):
        temp = self.cargo
        self.cargo = 0
        return temp