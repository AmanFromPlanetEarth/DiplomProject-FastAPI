from fastapi import FastAPI
from schema.user_shema import UserCreate
from routers.router import user_router, restaraunt_router
from database import engine
from models.model import UserModel, Model, RestaurantModel

app = FastAPI()

app.include_router(user_router)
app.include_router(restaraunt_router)

if __name__=="__main__":
    import uvicorn
    Model.metadata.create_all(engine)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)