import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("DATABASE_URL")
if not MONGODB_URL:
    raise Exception("Missing DATABASE_URL in environment variables.")

client = MongoClient(MONGODB_URL)
db = client.get_default_database()

# Clean old data
db.restaurants.delete_many({})
db.menu_items.delete_many({})

# Restaurant entries with slug-style IDs
restaurants = [
    {
        "id": "saffrongrill",
        "name": "Saffron Grill",
        "logo": "🍛",
        "theme": {"primary": "#FF5733", "secondary": "#FFC300"},
        "tables": {str(i): "empty" for i in range(1, 11)},
        "email": "owner@saffrongrill.com",
        "signup_status": "not_signed_up",
        "secret_signup_code": "SGRILL-2025"
    },
    {
        "id": "tokyobites",
        "name": "Tokyo Bites",
        "logo": "🍣",
        "theme": {"primary": "#1E1E1E", "secondary": "#E91E63"},
        "tables": {str(i): "empty" for i in range(1, 11)},
        "email": "admin@tokyobites.jp",
        "signup_status": "not_signed_up",
        "secret_signup_code": "TOKYO-2025"
    },
    {
        "id": "bellavista",
        "name": "Bella Vista",
        "logo": "🍝",
        "theme": {"primary": "#000000", "secondary": "#374151"},
        "tables": {str(i): "empty" for i in range(1, 11)},
        "email": "contact@bellavista.it",
        "signup_status": "not_signed_up",
        "secret_signup_code": "BELLA-2025"
    },
    {
        "id": "burgermafia",
        "name": "Burger Mafia",
        "logo": "🍔",
        "theme": {"primary": "#8B0000", "secondary": "#FF8C00"},
        "tables": {str(i): "empty" for i in range(1, 11)},
        "email": "support@burgermafia.com",
        "signup_status": "not_signed_up",
        "secret_signup_code": "MAFIA-2025"
    },
    {
        "id": "greenleaf",
        "name": "Green Leaf",
        "logo": "🥗",
        "theme": {"primary": "#2E7D32", "secondary": "#A5D6A7"},
        "tables": {str(i): "empty" for i in range(1, 11)},
        "email": "green@leaf.org",
        "signup_status": "not_signed_up",
        "secret_signup_code": "LEAFY-2025"
    }
]


db.restaurants.insert_many(restaurants)

# Menu items with new restaurantId references
menu_items = [
    # Saffron Grill
    {
        "id": "001", "name": "Butter Chicken",
        "description": "Rich tomato-based gravy with tender chicken pieces",
        "price": 14.99, "image": "https://images.pexels.com/photos/1111315/pexels-photo-1111315.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Indian", "isPopular": True, "isVegetarian": False, "restaurantId": "saffrongrill"
    },
    {
        "id": "002", "name": "Paneer Tikka",
        "description": "Grilled cottage cheese cubes with spices",
        "price": 10.50, "image": "https://images.pexels.com/photos/678414/pexels-photo-678414.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Indian", "isPopular": True, "isVegetarian": True, "restaurantId": "saffrongrill"
    },
    {
        "id": "003", "name": "Garlic Naan",
        "description": "Soft Indian bread with garlic butter",
        "price": 3.99, "image": "https://images.pexels.com/photos/128408/pexels-photo-128408.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Indian", "isPopular": False, "isVegetarian": True, "restaurantId": "saffrongrill"
    },

    # Tokyo Bites
    {
        "id": "004", "name": "Sushi Platter",
        "description": "Assorted fresh sushi with wasabi and soy sauce",
        "price": 25.00, "image": "https://images.pexels.com/photos/3577561/pexels-photo-3577561.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Japanese", "isPopular": True, "isVegetarian": False, "restaurantId": "tokyobites"
    },
    {
        "id": "005", "name": "Miso Soup",
        "description": "Traditional soup with tofu and seaweed",
        "price": 4.50, "image": "https://images.pexels.com/photos/6246437/pexels-photo-6246437.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Japanese", "isPopular": False, "isVegetarian": True, "restaurantId": "tokyobites"
    },
    {
        "id": "006", "name": "Chicken Teriyaki",
        "description": "Grilled chicken glazed with teriyaki sauce",
        "price": 18.75, "image": "https://images.pexels.com/photos/1124733/pexels-photo-1124733.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Japanese", "isPopular": True, "isVegetarian": False, "restaurantId": "tokyobites"
    },

    # Bella Vista
    {
        "id": "007", "name": "Truffle Pasta",
        "description": "Handmade pasta with black truffle and herbs",
        "price": 28.99, "image": "https://images.pexels.com/photos/1279330/pexels-photo-1279330.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Pasta", "isPopular": True, "isVegetarian": False, "restaurantId": "bellavista"
    },
    {
        "id": "008", "name": "Margherita Pizza",
        "description": "Wood-fired pizza with mozzarella and basil",
        "price": 22.50, "image": "https://images.pexels.com/photos/2147491/pexels-photo-2147491.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Pizza", "isPopular": False, "isVegetarian": True, "restaurantId": "bellavista"
    },
    {
        "id": "009", "name": "Grilled Salmon",
        "description": "Salmon with lemon butter sauce",
        "price": 32.00, "image": "https://images.pexels.com/photos/3622479/pexels-photo-3622479.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Seafood", "isPopular": False, "isVegetarian": False, "restaurantId": "bellavista"
    },

    # Burger Mafia
    {
        "id": "010", "name": "Cheeseburger",
        "description": "Beef patty with cheddar, onions and pickles",
        "price": 12.00, "image": "https://images.pexels.com/photos/1639562/pexels-photo-1639562.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Burger", "isPopular": True, "isVegetarian": False, "restaurantId": "burgermafia"
    },
    {
        "id": "011", "name": "Veggie Burger",
        "description": "Plant-based patty with lettuce and vegan mayo",
        "price": 10.00, "image": "https://images.pexels.com/photos/958545/pexels-photo-958545.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Burger", "isPopular": True, "isVegetarian": True, "restaurantId": "burgermafia"
    },
    {
        "id": "012", "name": "Onion Rings",
        "description": "Crispy golden onion rings",
        "price": 5.50, "image": "https://images.pexels.com/photos/1343503/pexels-photo-1343503.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Sides", "isPopular": False, "isVegetarian": True, "restaurantId": "burgermafia"
    },

    # Green Leaf
    {
        "id": "013", "name": "Caesar Salad",
        "description": "Romaine lettuce, parmesan, croutons, Caesar dressing",
        "price": 9.99, "image": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Salad", "isPopular": True, "isVegetarian": True, "restaurantId": "greenleaf"
    },
    {
        "id": "014", "name": "Avocado Toast",
        "description": "Multigrain bread topped with smashed avocado",
        "price": 7.25, "image": "https://images.pexels.com/photos/5732856/pexels-photo-5732856.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Breakfast", "isPopular": True, "isVegetarian": True, "restaurantId": "greenleaf"
    },
    {
        "id": "015", "name": "Quinoa Bowl",
        "description": "Quinoa, grilled veggies, hummus and tahini",
        "price": 12.50, "image": "https://images.pexels.com/photos/1640770/pexels-photo-1640770.jpeg?auto=compress&cs=tinysrgb&w=500",
        "category": "Healthy", "isPopular": False, "isVegetarian": True, "restaurantId": "greenleaf"
    }
]

db.menu_items.insert_many(menu_items)

print("✅ 5 restaurants with username-style IDs and menus inserted successfully.")
