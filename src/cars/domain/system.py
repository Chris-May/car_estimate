from eventsourcing.system import System

from cars.domain.application import CarApplication


class CarSystem(System):
    def initialize(self) -> None:
        super().__init__(
            pipes=[
                [CarApplication],
            ]
        )
