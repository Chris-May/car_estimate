import logging
from datetime import UTC, datetime

from eventsourcing.application import ProcessingEvent
from eventsourcing.dispatch import singledispatchmethod
from eventsourcing.domain import DomainEventProtocol
from eventsourcing.system import ProcessApplication

from cars.common.db import sqlite_insert
from cars.domain.car import Car

logger = logging.getLogger(__name__)

sqlite_insert(
    """
    CREATE TABLE IF NOT EXISTS awaiting_history (
        car_id STRING PRIMARY KEY,
        make STRING,
        model STRING,
        year INTEGER,
        vin STRING,
        plate STRING,
        added_at TIMESTAMP
    )
    """
)


class AwaitingHistoryViewModel(ProcessApplication):
    @singledispatchmethod
    def policy(
        self, domain_event: DomainEventProtocol, processing_event: ProcessingEvent
    ) -> None:
        logger.warning(
            'Unexpected dispatch event: %s %s', domain_event, processing_event
        )

    @policy.register(Car.Created)
    def _(self, domain_event: Car.Created, _):
        sqlite_insert(
            """
        INSERT INTO awaiting_history (car_id, make, model, year, vin, plate, added_at)
        VALUES (?,?,?,?,?,?,?)
        """,
            (
                domain_event.originator_id.hex,
                domain_event.make,
                domain_event.model,
                domain_event.year,
                domain_event.vin,
                domain_event.plate,
                datetime.now(tz=UTC).timestamp(),
            ),
        )

    @policy.register(Car.HistoryAdded)
    def remove_from_database(self, domain_event: Car.HistoryAdded, _):
        sqlite_insert(
            'DELETE FROM awaiting_history WHERE car_id = ?',
            (domain_event.originator_id.hex,),
        )
