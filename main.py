from fastapi import FastAPI
from schema.user_shema import UserCreate
from routers.router import user_router, restaraunt_router
from database import engine
from models.model import UserModel

app = FastAPI()

app.include_router(user_router)
app.include_router(restaraunt_router)

@app.get("/")
def root(name: str):
    return {"Hello": f"{name}"}


if __name__=="__main__":
    import uvicorn
    UserModel.metadata.create_all(engine)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)