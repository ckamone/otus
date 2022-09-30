from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=500, started=False, fuel=100, fuel_consumption=10):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel == 0:
                raise LowFuelError(f"Топливо на нуле: {self.fuel}")
            else:
                self.started = True

    def move(self, km: int):
        self.start()
        if km / self.fuel_consumption <= self.fuel:
            self.fuel -= km / self.fuel_consumption
            return 'SUCCESS'
        else:
            raise NotEnoughFuel(f"Недостаточно топлива. Для дистанции {km}км с расходом {self.fuel_consumption}л/100км" \
                                f" не хватит того, что в баке (требуется={km / self.fuel_consumption}л, в баке={self.fuel}л)")


