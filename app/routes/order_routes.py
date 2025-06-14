from fastapi import APIRouter, HTTPException, Depends
from app.models.order_models import OrderModel, OrderItemModel
from app.database import get_database
from typing import List

router = APIRouter()

@router.post("/orders")
def place_order(order: dict, db=Depends(get_database)):
    # Convert incoming dict to OrderModel
    items = [OrderItemModel(**item) for item in order.get("items", [])]
    order_obj = OrderModel(
        restaurantId=order["restaurantId"],
        table=order["table"],
        items=items,
        total=order["total"]
    )
    result = db.orders.insert_one(order_obj.to_dict())
    return {"orderId": str(result.inserted_id), "status": "pending"}
