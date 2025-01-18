from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable

from eventsourcing.domain import Aggregate

class Entry: ...

class Car(Aggregate):
    def __init__(self, make:str, model:str, plate: str, vin:str, year: int, ):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.plate = plate
        self.history_log:list[Entry] = []
        self.estimate: int | None = None

    def add_history_entry(self, log: Iterable[Entry]):
        self.history_log.extend(log)

    def add_estimate(self, estimate:Decimal):
        self.estimate = estimate
