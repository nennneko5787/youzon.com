from pydantic import BaseModel

from .ItemTypes import ItemTypes


class Item(BaseModel):
    id: int
    name: str
    type: ItemTypes
    price: int
    summary: str
    description: str
    image: str
