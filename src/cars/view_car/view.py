from uuid import UUID

from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import StreamingResponse

from cars.templating import templates

car_view_router = APIRouter()


@car_view_router.get('/cars/{car_id}', include_in_schema=False)
async def view_car(car_id: UUID, request: Request):
    app = request.state.app
    car = app.get_car(car_id)
    template = templates.get_template('view_car.html')
    return StreamingResponse(template.generate_async(dict(car=car)))
