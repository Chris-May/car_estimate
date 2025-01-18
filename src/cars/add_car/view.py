from fastapi import APIRouter
from starlette.requests import Request

from cars.templating import templates

add_car_router = APIRouter()


@add_car_router.get('/', include_in_schema=False)
def add_car_form(request: Request):
    return templates.TemplateResponse(
        request=request, name='add_car.html', context={'request': request}
    )


@add_car_router.post('/', include_in_schema=False)
def add_car(request: Request): ...
