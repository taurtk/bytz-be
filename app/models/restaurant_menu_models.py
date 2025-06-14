from typing import Optional, List, Dict

class RestaurantModel:
    def __init__(self, id: str, name: str, logo: str, theme: Dict[str, str], tables: Dict[str, str]):
        self.id = id
        self.name = name
        self.logo = logo
        self.theme = theme
        self.tables = tables  # Dict[str, str] where key is table number, value is 'empty' or 'full'

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "logo": self.logo,
            "theme": self.theme,
            "tables": self.tables
        }

class MenuItemModel:
    def __init__(self, id: str, name: str, description: str, price: float, image: str, category: str, isPopular: Optional[bool] = False, isVegetarian: Optional[bool] = False, restaurantId: Optional[str] = None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.category = category
        self.isPopular = isPopular
        self.isVegetarian = isVegetarian
        self.restaurantId = restaurantId

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image": self.image,
            "category": self.category,
            "isPopular": self.isPopular,
            "isVegetarian": self.isVegetarian,
            "restaurantId": self.restaurantId
        }
