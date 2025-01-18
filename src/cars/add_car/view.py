from fastapi import APIRouter
from starlette.templating import Jinja2Templates

add_car_router = APIRouter()
templates = Jinja2Templates(directory='templates')


@add_car_router.get('/', include_in_schema=False)
def add_car_form(): ...
