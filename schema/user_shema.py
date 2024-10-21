from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: int

class UserUpdate(BaseModel):
    name: str
    phone: int

class RestaurantCreate(BaseModel):
    name: str
    owner_id: int

class RestaurantUpdate(BaseModel):
    name: str
    owner_id: int
