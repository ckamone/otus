from abc import ABC

from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weigth: int = 500
    started: bool = False
    fuel: int = 100
    fuel_consumption: int = 10

    def __init__(self, weight, started, fuel, fuel_consumption):
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
