from order_publisher.publisher import Publisher
from order_publisher.generator import OrderGenerator
from api.controller.request_parser import RequestParser
from api.model import Model


from flask import (
    Blueprint,
    Response, 
    request,
    jsonify
)

controller_bp = Blueprint("controller", __name__)
order_generator = OrderGenerator(r"src/order_publisher/conf/generator_conf.json")
publisher = Publisher(r"src/order_publisher/conf/publisher_conf.json")


@controller_bp.route("/orders/generate", methods=["POST"])
def generate_and_send_orders() -> Response:
    """
    Handles the generation and publishing of orders via a POST request. It parses the input request,
    validates it, and calls the order generation and publishing process.

    Raises:
        ValueError: If the input request body is empty or invalid.

    Returns:
        Response: 
            - A JSON response containing the list of generated order IDs with a status code 200 if successful.
            - A JSON response with the error message and status code 400 if an exception occurs.
    """
    try:
        json_request = request.get_json(silent=True)
        if json_request is None:
            raise ValueError("The given request is empty!")
        RequestParser(**json_request)
        orders = Model.generate_and_publish_orders(
            orders_to_generate= json_request["orders_to_generate"], 
            order_generator= order_generator, 
            publisher= publisher
        )
        return jsonify({"orders":orders}), 200
    except Exception as e:
        return jsonify({"Exception!": str(e)}), 400