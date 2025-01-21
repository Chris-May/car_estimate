import asyncio
import logging

import httpx
from eventsourcing.system import SingleThreadedRunner

from cars.common.db import sqlite_execute
from cars.domain.application import CarApplication
from cars.domain.system import CarSystem

logger = logging.getLogger(__name__)
connection_limit = asyncio.Semaphore(5)
client = httpx.AsyncClient()
HISTORY_URL = 'http://localhost:8000/data/'


def select_oldest_entries(limit: int = 100) -> list[dict]:
    return sqlite_execute(
        'SELECT * FROM awaiting_history ORDER BY added_at ASC LIMIT ?', (limit,)
    )


async def get_history_for_car(make, model, year, vin, plate):
    headers = {'Content-Type': 'application/json'}
    async with connection_limit:
        r = await client.get(
            HISTORY_URL,
            headers=headers,
            params=dict(make=make, model=model, year=year, vin=vin, plate=plate),
        )

        if connection_limit.locked():
            await asyncio.sleep(1)

        return r.json()


async def process_car_data(entry, application):
    car_id, make, model, year, vin, plate, _ = entry
    car_history = await get_history_for_car(make, model, year, vin, plate)
    application.add_history(car_id=car_id, log=car_history)
    return car_id  # Or other info if needed for further use


async def main():
    runner = SingleThreadedRunner(system=CarSystem())
    runner.start()
    app = runner.get(CarApplication)

    entries = select_oldest_entries()
    await asyncio.gather(*[process_car_data(entry, app) for entry in entries])
    logger.info('Finished processing %s entries', len(entries))


if __name__ == '__main__':
    asyncio.run(main())
