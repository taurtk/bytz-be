from fastapi import APIRouter, HTTPException, Depends
from app.models.restaurant_menu_models import RestaurantModel, MenuItemModel
from app.database import get_database
from typing import List

router = APIRouter()

@router.get("/restaurants", response_model=List[dict])
def get_restaurants(db=Depends(get_database)):
    restaurants = list(db.restaurants.find())
    for r in restaurants:
        r.pop("_id", None)
    return restaurants

@router.get("/restaurants/{restaurant_id}", response_model=dict)
def get_restaurant(restaurant_id: str, db=Depends(get_database)):
    
    restaurant = db.restaurants.find_one({"id": restaurant_id})
    print(restaurant)

    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    restaurant.pop("_id", None)
    return restaurant

@router.get("/restaurants/{restaurant_id}/menu", response_model=List[dict])
def get_menu(restaurant_id: str, db=Depends(get_database)):
    items = list(db.menu_items.find({"restaurantId": restaurant_id}))
    for item in items:
        item.pop("_id", None)
    return items

@router.get("/restaurants/{restaurant_id}/categories", response_model=List[str])
def get_categories(restaurant_id: str, db=Depends(get_database)):
    items = db.menu_items.find({"restaurantId": restaurant_id})
    categories = set()
    for item in items:
        if 'category' in item:
            categories.add(item['category'])
    return ["All"] + sorted(categories)
