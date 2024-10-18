from pydantic import BaseModel


class Customer(BaseModel):
    customer_id_min: int
    customer_id_max: int
    

class OrderItems(BaseModel):
    min_order_items: int
    max_order_items: int


class Item(BaseModel):
    item_id_min: int
    item_id_max: int
    

class Tags(BaseModel):
    min_tags: int
    max_tags: int
    tag_id_min: int
    tag_id_max: int
    

class City(BaseModel):
    city_id_min: int
    city_id_max: int


class GeneratorConfSchema(BaseModel):
    customer: Customer
    order_items: OrderItems
    item: Item
    tags: Tags
    city: City