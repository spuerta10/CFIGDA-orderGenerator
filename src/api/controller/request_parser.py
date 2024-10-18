from pydantic import BaseModel


class RequestParser(BaseModel):
    orders_to_generate: int