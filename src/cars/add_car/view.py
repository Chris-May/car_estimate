from typing import Annotated

from fastapi import APIRouter, Form
from pydantic import BaseModel
from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse

from cars.templating import templates

add_car_router = APIRouter()


@add_car_router.get('/', include_in_schema=False)
def add_car_form(request: Request):
    return templates.TemplateResponse(
        request=request, name='add_car.html', context={'request': request}
    )


class AddCarForm(BaseModel):
    make: str
    model: str
    year: int
    plate: str
    vin: str


@add_car_router.post('/', include_in_schema=False)
def add_car(request: Request, data: Annotated[AddCarForm, Form()]):
    app = request.state.app
    car = app.add_car(**data.model_dump())
    return RedirectResponse(f'/cars/{car.id}', status_code=status.HTTP_303_SEE_OTHER)
