from typing import List
from datetime import datetime

class OrderItemModel:
    def __init__(self, itemId: str, quantity: int, name: str, price: float):
        self.itemId = itemId
        self.quantity = quantity
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "itemId": self.itemId,
            "quantity": self.quantity,
            "name": self.name,
            "price": self.price
        }

class OrderModel:
    def __init__(self, restaurantId: str, table: str, items: List[OrderItemModel], total: float, status: str = "pending", createdAt: str = None):
        self.restaurantId = restaurantId
        self.table = table
        self.items = [item.to_dict() for item in items]
        self.total = total
        self.status = status
        self.createdAt = createdAt or datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "restaurantId": self.restaurantId,
            "table": self.table,
            "items": self.items,
            "total": self.total,
            "status": self.status,
            "createdAt": self.createdAt
        }
