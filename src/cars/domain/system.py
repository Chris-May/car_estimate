from add_estimate.processor import GetEstimateProcessor
from eventsourcing.system import System

from cars.add_history.view_model import AwaitingHistoryViewModel
from cars.domain.application import CarApplication


class CarSystem(System):
    def __init__(self) -> None:
        super().__init__(
            pipes=[
                [CarApplication, AwaitingHistoryViewModel, GetEstimateProcessor],
                [CarApplication, GetEstimateProcessor],
            ]
        )
