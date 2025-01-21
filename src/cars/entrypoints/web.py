from contextlib import asynccontextmanager
from typing import TypedDict

from common.examples import other
from eventsourcing.system import MultiThreadedRunner
from fastapi import FastAPI

from cars.add_car.view import add_car_router
from cars.domain.application import CarApplication
from cars.domain.system import CarSystem
from cars.view_car.view import car_view_router


class State(TypedDict):
    app: CarApplication


@asynccontextmanager
async def lifespan(app: FastAPI):
    runner = MultiThreadedRunner(CarSystem())
    runner.start()
    app = runner.get(CarApplication)
    yield dict(app=app)
    runner.stop()


app = FastAPI(lifespan=lifespan)

for router in (add_car_router, car_view_router, other):
    app.include_router(router)
