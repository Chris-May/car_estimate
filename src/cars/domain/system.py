from eventsourcing.system import System

from cars.domain.application import CarApplication


class CarSystem(System):
    def __init__(self) -> None:
        super().__init__(
            pipes=[
                [CarApplication],
            ]
        )
