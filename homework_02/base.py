from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    # атрибуты со значениями по умолчанию
    weight = 500
    fuel = 100
    fuel_consumption = 10
    started = False  #

    def __init__(self, weight=500, fuel=100, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError(f"Топливо на нуле: {self.fuel}")


    def move(self, km: int):
        self.start()
        if km / self.fuel_consumption <= self.fuel:
            self.fuel -= km / self.fuel_consumption
            return 'SUCCESS'
        else:
            raise NotEnoughFuel(f"Недостаточно топлива. Для дистанции {km}км с расходом {self.fuel_consumption}л/100км" \
                                f" не хватит того, что в баке (требуется={km / self.fuel_consumption}л, в баке={self.fuel}л)")


