from flask import Blueprint

products_app = Blueprint(
    "products_app",
    __name__,
)


@products_app.route("/")
def products_list():
    return [
        "P1",
        "P2",
        "P3",
    ]
