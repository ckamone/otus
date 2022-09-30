"""
создайте класс `Car`, наследник `Vehicle`
"""
from engine import Vehicle


class Car(Vehicle):
    engine: Vehicle

    def set_engine(self, volume, pistons):
        self.engine = Vehicle(volume=volume, pistons=pistons)
