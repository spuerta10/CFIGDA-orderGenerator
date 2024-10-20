""" Module to generate Mock Orders data
"""
from uuid import uuid4
from random import randint, uniform

from credit_risk_lib.config.config import Config
from credit_risk_lib.config.config_factory import ConfigFactory 
from pydantic import BaseModel


class OrderGenerator:
    def __init__(self, generator_conf_path: str, generator_conf_schema: BaseModel = None): 
        """Initialize the OrderGenerator with configuration.

        Args:
            generator_conf_path (str): The path to the configuration file for the generator.
            generator_conf_schema (BaseModel, optional): An optional schema for validating the configuration.
                Defaults to None.
        """
        self._conf: Config = ConfigFactory.get_conf(generator_conf_path, generator_conf_schema)
    
    
    def generate(self) -> dict:
        # TODO: Could look into dbldatagen lib for generating data
        """Generate a random order.

        This method creates an order dictionary with a unique order ID, a random customer ID,
        a list of order items, and a random city ID based on the configuration settings.

        Returns:
            dict: A dictionary representing the generated order, containing keys such as 
            'customer_id', 'order_id', 'order_items', and 'city_id'.
        """
        order = {
            "customer_id": randint(self._conf.customer["customer_id_min"],self._conf.customer["customer_id_max"]),
            "order_id": str(uuid4()),  # generate an UUID 4 unique order identifier
            "order_items": self._generate_order_items(),
            "city_id": randint(self._conf.city["city_id_min"], self._conf.city["city_id_max"]),
            "total_amount": round(
                uniform(
                    self._conf.total_amount["min_total_amount"],
                    self._conf.total_amount["max_total_amount"]
                ), 2
            ),
            "payment_method_id": randint(
                self._conf.payment_method["payment_method_id_min"],
                self._conf.payment_method["payment_method_id_max"]
            )
        }
        return order
    
    
    def _generate_order_items(self) -> list[dict]:
        """Generate a list of order items.

        This method creates a list of dictionaries, where each dictionary represents an order item
        with a randomly assigned item ID and a list of associated tags.

        Returns:
            list[dict]: A list of dictionaries, each containing 'item_id' and 'item_tags'.
        """
        items_number =  randint(
            self._conf.order_items["min_order_items"],
            self._conf.order_items["max_order_items"]
        )  # random number of items placed in the order
        items = [
            {
                "item_id": randint(self._conf.item["item_id_min"], self._conf.item["item_id_max"]),
                "item_tags": self._generate_item_tags()
            }
            for _ in range(items_number)
        ]
        return items


    def _generate_item_tags(self) -> list[int]:
        """Generate a list of item tags.

        This method creates a list of integers, where each integer represents a tag ID.
        The number of tags is randomly determined based on configuration settings.

        Returns:
            list[int]: A list of integers representing tag IDs associated with an item.
        """
        tags_number = randint(
           self._conf.tags["min_tags"],
           self._conf.tags["max_tags"] 
        )  # random number of tags to be placed for each item in the order
        return [
            randint(
                self._conf.tags["tag_id_min"],
                self._conf.tags["tag_id_max"]
            )
            for _ in range(tags_number)
        ]
