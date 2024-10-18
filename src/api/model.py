from order_publisher.publisher import Publisher
from order_publisher.generator import OrderGenerator


class Model:
    @classmethod
    def generate_and_publish_orders(
        cls,
        orders_to_generate: int,
        order_generator: OrderGenerator,
        publisher: Publisher
    ) -> 'Model':
        orders = []  # TODO: delete this 
        for _ in range(orders_to_generate):
           order: dict= order_generator.generate()
           #publisher.publish(order)
           orders.append(order)  # TODO: delete this
           
        return orders
    