from order_publisher.publisher import Publisher
from order_publisher.generator import OrderGenerator


class Model:
    @classmethod
    def generate_and_publish_orders(
        cls,
        orders_to_generate: int,
        order_generator: OrderGenerator,
        publisher: Publisher
    ) -> list[str]:
        """
        Generates a specified number of orders using the provided order generator,
        publishes each order using the provided publisher, and returns a list of the generated order IDs.

        Args:
            orders_to_generate (int): The number of orders to generate and publish.
            order_generator (OrderGenerator): An instance responsible for generating order dictionaries.
            publisher (Publisher): An instance responsible for publishing the generated orders.

        Returns:
            list[str]: A list of order IDs from the generated and published orders.
        """
        orders: list[str] = []
        for _ in range(orders_to_generate):
           order: dict= order_generator.generate()
           publisher.publish(order)
           orders.append(order["order_id"])
           
        return orders
    