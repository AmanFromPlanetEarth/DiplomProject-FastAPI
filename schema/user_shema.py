from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str | None = None
    phone: int | None = None

class UserUpdate(BaseModel):
    name: str = None
    phone: int = None

class RestaurantCreate(BaseModel):
    pass

class RestaurantUpdate(BaseModel):
    pass
