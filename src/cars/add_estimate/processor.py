import logging
from decimal import Decimal

import httpx
from eventsourcing.application import ProcessingEvent
from eventsourcing.domain import DomainEventProtocol
from eventsourcing.system import ProcessApplication

from cars.domain.application import add_estimate_to_car
from cars.domain.car import Car

logger = logging.getLogger(__name__)
ESTIMATE_URL = 'http://localhost:8000/data/estimate'


class GetEstimateProcessor(ProcessApplication):
    def policy(
        self, domain_event: DomainEventProtocol, processing_event: ProcessingEvent
    ) -> None:
        if isinstance(domain_event, Car.HistoryAdded):
            car = self.repository.get(domain_event.originator_id)
            result = httpx.get(
                ESTIMATE_URL,
                params=dict(
                    make=car.make,
                    model=car.model,
                    year=car.year,
                    vin=car.vin,
                    plate=car.plate,
                    history_log=car.history_log,
                ),
                timeout=60,
            )
            data = result.json()
            add_estimate_to_car(car.id.hex, Decimal(data['estimate']))
