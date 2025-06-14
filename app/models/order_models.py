from typing import List

class OrderItemModel:
    def __init__(self, itemId: str, quantity: int):
        self.itemId = itemId
        self.quantity = quantity

    def to_dict(self):
        return {
            "itemId": self.itemId,
            "quantity": self.quantity
        }

class OrderModel:
    def __init__(self, restaurantId: str, table: str, items: List[OrderItemModel], total: float, status: str = "pending"):
        self.restaurantId = restaurantId
        self.table = table
        self.items = [item.to_dict() for item in items]
        self.total = total
        self.status = status

    def to_dict(self):
        return {
            "restaurantId": self.restaurantId,
            "table": self.table,
            "items": self.items,
            "total": self.total,
            "status": self.status
        }
