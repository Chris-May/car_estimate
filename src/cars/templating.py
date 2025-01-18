import jinja2
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(
    directory='entrypoints/templates',
    loader=jinja2.ChoiceLoader(
        [
            jinja2.PackageLoader('cars.entrypoints', 'templates'),
            jinja2.PackageLoader('cars.add_car', 'templates'),
        ]
    ),
)
