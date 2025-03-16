from contextlib import asynccontextmanager
from typing import TypedDict

from eventsourcing.system import MultiThreadedRunner, Runner
from fastapi import FastAPI
from starlette.requests import Request

from cars.add_car.view import add_car_router
from cars.common.examples import other
from cars.domain.application import CarApplication
from cars.domain.system import CarSystem
from cars.view_car.view import car_view_router


class State(TypedDict):
    app: CarApplication
    runner: Runner


@asynccontextmanager
async def lifespan(app: FastAPI):
    runner = MultiThreadedRunner(CarSystem())
    runner.start()
    app = runner.get(CarApplication)
    yield dict(app=app, runner=runner)
    runner.stop()


app = FastAPI(lifespan=lifespan)

for router in (add_car_router, car_view_router, other):
    app.include_router(router)


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    # update_followers(request.state.runner)
    return response
