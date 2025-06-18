from fastapi import APIRouter, HTTPException, Depends
from app.models.order_models import OrderModel, OrderItemModel
from app.database import get_database
from typing import List
from bson import ObjectId

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

@router.get("/orders/{restaurant_id}", response_model=List[dict])
def get_orders(restaurant_id: str, db=Depends(get_database)):
    orders = list(db.orders.find({"restaurantId": restaurant_id}))
    # Remove _id or convert to string for serialization
    for order in orders:
        order["id"] = str(order.pop("_id"))
    return orders

@router.put("/orders/{order_id}/complete")
def mark_order_completed(order_id: str, db=Depends(get_database)):
    result = db.orders.update_one({"_id": ObjectId(order_id)}, {"$set": {"status": "completed"}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"success": True, "orderId": order_id, "status": "completed"}
