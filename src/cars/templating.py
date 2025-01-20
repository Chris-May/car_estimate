import jinja2
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(
    env=jinja2.Environment(
        enable_async=True,
        autoescape=True,
        loader=jinja2.ChoiceLoader(
            [
                jinja2.PackageLoader('cars.entrypoints', 'templates'),
                jinja2.PackageLoader('cars.add_car', 'templates'),
                jinja2.PackageLoader('cars.view_car', 'templates'),
            ]
        ),
    ),
)
