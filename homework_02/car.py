"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine


class Car(Vehicle):
    engine: Vehicle

    def set_engine(self, volume, pistons):
        self.engine = Engine(volume=volume, pistons=pistons)
