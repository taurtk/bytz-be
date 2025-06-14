import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("DATABASE_URL")
client = MongoClient(MONGODB_URL)
db = client.get_default_database()

# Insert a sample restaurant
db.restaurants.insert_one({
    "id": "resto1",
    "name": "Bella Vista",
    "logo": "🍝",
    "theme": {"primary": "#000000", "secondary": "#374151"},
    "tables": 10
})

# Insert a few sample menu items
db.menu_items.insert_many([
    {
        "id": "001",
        "name": "Truffle Pasta",
        "description": "Handmade pasta with black truffle, parmesan, and fresh herbs",
        "price": 28.99,
        "image": "https://images.pexels.com/photos/1279330/pexels-photo-1279330.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Pasta",
        "isPopular": True,
        "isVegetarian": False,
        "restaurantId": "resto1"
    },
    {
        "id": "002",
        "name": "Margherita Pizza",
        "description": "Classic wood-fired pizza with fresh mozzarella, tomatoes, and basil",
        "price": 22.50,
        "image": "https://images.pexels.com/photos/2147491/pexels-photo-2147491.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Pizza",
        "isPopular": False,
        "isVegetarian": True,
        "restaurantId": "resto1"
    },
    {
        "id": "003",
        "name": "Grilled Salmon",
        "description": "Atlantic salmon with lemon butter sauce and seasonal vegetables",
        "price": 32.00,
        "image": "https://images.pexels.com/photos/3622479/pexels-photo-3622479.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Seafood",
        "isPopular": False,
        "isVegetarian": False,
        "restaurantId": "resto1"
    }
])

print("Sample restaurant and menu items inserted.")
