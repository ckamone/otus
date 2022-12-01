from flask import Blueprint, render_template

products_app = Blueprint(
    "products_app",
    __name__,
)

PRODUCTS = {
    1: "Laptop",
    2: "Mouse",
    3: "Keyboard",
    4: "Tablet",
    5: "Smartphone",
}
@products_app.route("/", endpoint="list")
def products_list():
    return render_template(
        "products/list.html",
        products=PRODUCTS.items(),
    )

@products_app.route("/<int:product_id>/", endpoint="details")
def get_product_by_id(product_id: int):
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        raise FileNotFoundError(f"Product #{product_id} not found")
    return render_template(
        "products/details.html",
        product_id=product_id,
        product_name=product_name,
    )