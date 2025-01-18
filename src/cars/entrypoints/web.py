from fastapi import FastAPI

from src.cars.add_car.view import add_car_router

app = FastAPI()

for router in (add_car_router,):
    app.include_router(router)
