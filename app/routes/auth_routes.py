from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from app.database import get_database
from datetime import datetime

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class SignupCredentials(BaseModel):
    email: EmailStr
    password: str
    retailerId: str
    secretCode: str

class SigninCredentials(BaseModel):
    email: EmailStr
    password: str

@router.post("/signup")
def signup(credentials: SignupCredentials, db=Depends(get_database)):
    # Check if email already exists
    if db.restaurants_auth.find_one({"email": credentials.email}):
        raise HTTPException(status_code=400, detail="Email already exists.")
    # Fetch restaurant by retailerId
    restaurant_record = db.restaurants.find_one({"id": credentials.retailerId})
    print(restaurant_record)
    if not restaurant_record:
        raise HTTPException(status_code=404, detail="Restaurant not found.")
    # Check email and secret code match
    if restaurant_record.get("email") != credentials.email or restaurant_record.get("secret_signup_code") != credentials.secretCode:
        raise HTTPException(status_code=400, detail="Email or secret code does not match restaurant records.")
    password_hash = pwd_context.hash(credentials.password)
    restaurant = {
        "email": credentials.email,
        "password_hash": password_hash,
        "retailerId": credentials.retailerId,
        "isActive": True,
        "createdAt": datetime.utcnow().isoformat()
    }
    result = db.restaurants_auth.insert_one(restaurant)
    user = db.restaurants_auth.find_one({"_id": result.inserted_id})
    response_restaurant = {k: v for k, v in user.items() if k not in ["password_hash", "_id"]}
    response_restaurant["id"] = str(user["_id"])
    return {"success": True, "restaurant": response_restaurant}

@router.post("/signin")
def signin(credentials: SigninCredentials, db=Depends(get_database)):
    user = db.restaurants_auth.find_one({"email": credentials.email})
    if not user or not pwd_context.verify(credentials.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password.")
    response_user = {k: v for k, v in user.items() if k not in ["password_hash", "_id", "secretCode"]}
    response_user["id"] = str(user["_id"])
    return {"success": True, "restaurant": response_user}
