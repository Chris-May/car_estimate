from collections.abc import Iterable
from decimal import Decimal
from uuid import UUID

from eventsourcing.application import Application

from src.cars.domain.car import Car, Entry


class CarApplication(Application):
    def get_car(self, car_id: UUID) -> Car:
        return self.repository.get(car_id)

    def add_car(self, make: str, model: str, plate: str, vin: str, year: int) -> Car:
        car = Car(make, model, plate, vin, year)
        self.save(car)
        return car

    def add_history(self, car_id: str, log: Iterable[Entry]) -> Car:
        car = self.repository.get(UUID(car_id))
        car.add_history(log)
        self.save(car)
        return car

    def add_estimate(self, car_id: str, estimate: Decimal) -> Car:
        car = self.repository.get(UUID(car_id))
        car.add_estimate(estimate)
        self.save(car)
        return car
