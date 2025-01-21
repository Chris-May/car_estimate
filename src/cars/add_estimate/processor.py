import logging

import httpx
from eventsourcing.application import ProcessingEvent
from eventsourcing.domain import DomainEventProtocol
from eventsourcing.system import ProcessApplication

from cars.domain.car import Car

logger = logging.getLogger(__name__)
ESTIMATE_URL = 'http://localhost:8000/data/estimate'


class GetEstimateProcessor(ProcessApplication):
    def policy(
        self, domain_event: DomainEventProtocol, processing_event: ProcessingEvent
    ) -> None:
        logger.warning('processing events: %s %s', domain_event, processing_event)
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
            )
            data = result.json()
            car.add_estimate(data['estimate'])
            self.save(car)
