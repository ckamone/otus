from abc import ABC

from exceptions import LowFuelError, NotEnoughFuel


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
        if km / self.fuel_consumption <= self.fuel:
            self.fuel -= km / self.fuel_consumption
        else:
            raise NotEnoughFuel(f"Недостаточно топлива. Для дистанции {km} с расходом {self.fuel_consumption}"
                                f"не хватит того, что в баке ({self.fuel})")
