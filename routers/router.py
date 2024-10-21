from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.orm import Session
from schema.user_shema import UserCreate
from models.model import UserModel, RestaurantModel
from schema.user_shema import UserCreate,UserUpdate, RestaurantCreate, RestaurantUpdate
from database import engine
from sqlalchemy import select, insert, update, delete


user_router = APIRouter(prefix="/users", tags=['Users'])
restaraunt_router = APIRouter(prefix="/restaraunt", tags=['Restaraunt'])

#Пользователи
@user_router.get(path="/get_user/")
def get_user(request: Request, user_id: int):
    session = Session(engine)
    stmt = select(UserModel).where(UserModel.id == user_id)
    result = session.execute(stmt)
    user = result.scalars().all()
    session.close()
    return user


@user_router.post(path="/create_user/")
def create_user(request: Request, user: UserCreate):
    session = Session(engine)
    is_user = session.execute(select(UserModel).where(UserModel.phone == user.phone)).scalar_one_or_none()
    if is_user:
        raise HTTPException(status_code=400, detail="Email уже существует")
    stmt = insert(UserModel).values(name = user.name,
                                    phone = user.phone)
    session.execute(stmt)
    session.commit()
    session.close()
    return user


@user_router.put(path="/update_user/")
def user_update(request:Request, user_id: int, new_user: UserUpdate):
    session = Session(engine)
    stmt = update(UserModel).where(UserModel.id == user_id).values(
        name = new_user.name,
        phone = new_user.phone
    )
    user = session.execute(stmt)
    session.commit()
    session.close()
    return user


@user_router.delete(path="/delete_user/")
def user_delete(request: Request, user_id:int):
    session = Session(engine)
    stmt = delete(UserModel).where(UserModel.id == user_id)
    result = session.execute(stmt)
    session.commit()
    session.close()
    return result

#Рестораны
@restaraunt_router.post(path="/create_restaurant/")
def add_restaurant(request: Request, restaurant: RestaurantCreate):
    session = Session(engine)
    stmt = insert(RestaurantModel).values(name = restaurant.name,
                                          owner_id = restaurant.owner_id)
    session.execute(stmt)
    session.commit()
    session.close()
    return restaurant


@restaraunt_router.get(path="/get_restaurant/")
def get_restaurant(request: Request, user_id: int):
    session = Session(engine)
    stmt = select(RestaurantModel).where(RestaurantModel.owner_id == user_id)
    result = session.execute(stmt)
    restaurant = result.scalars().all()
    session.close()
    return restaurant
