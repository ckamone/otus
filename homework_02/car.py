"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    engine = None

    def set_engine(self, volume, pistons):
        self.engine = Engine(volume=volume, pistons=pistons)

    def __str__(self):
        try:
            enj = self.engine
            return f'{Car.__name__} with: engine volume={enj.volume},engine pistons={enj.pistons}; weight={self.weight}, fuel={self.fuel},' \
                   f'consumption={self.fuel_consumption}, started={str(self.started)}'
        except Exception:
            return f'{Car.__name__} with: no engine info; weight={self.weight}, fuel={self.fuel},' \
                   f'consumption={self.fuel_consumption}, started={str(self.started)}'
