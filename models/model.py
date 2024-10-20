from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Model(DeclarativeBase):
    pass

class UserModel(Model):
    __tablename__="users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    restaurants = relationship("RestaurantModel", back_populates="owner")
    

class RestaurantModel(Model):
    __tablename__ = "restaurants"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    owner = relationship("UserModel", back_populates="restaurants")