"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine: Vehicle

    def set_engine(self, volume, pistons):
        self.engine = Engine(volume=volume, pistons=pistons)
