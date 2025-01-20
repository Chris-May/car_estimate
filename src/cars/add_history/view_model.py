import logging
import sqlite3

from eventsourcing.dispatch import singledispatchmethod
from eventsourcing.system import ProcessApplication

from cars.domain.car import Car

logger = logging.getLogger(__name__)
DATABASE_LOCATION = 'cars.sqlite'
conn = sqlite3.connect(DATABASE_LOCATION)

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS cars (
    car_id STRING PRIMARY KEY,
    make STRING,
    model STRING,
    year INTEGER,
    vin STRING PRIMARY KEY,
    plate STRING
)
""")
conn.commit()
conn.close()


class AwaitingHistoryViewModel(ProcessApplication):
    @singledispatchmethod
    def dispatch(self, event, process):
        logger.warning('Unexpected dispatch event: %s %S', event, process)

    @dispatch.register('Car.Created')
    def add_to_database(self, event: Car.Created, _):
        cursor = conn.cursor()
        cursor.execute(
            """
        INSERT INTO cars (car_id, make, model, year, vin, plate) VALUES (?,?,?,?,?,?)
        """,
            (
                event.originator_id,
                event.make,
                event.model,
                event.year,
                event.vin,
                event.plate,
            ),
        )
        conn.commit()
        conn.close()

    @dispatch.register('Car.HistoryAdded')
    def remove_from_database(self, event: Car.HistoryAdded, _):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cars WHERE car_id = ?', event.originator_id)
        conn.commit()
        conn.close()
