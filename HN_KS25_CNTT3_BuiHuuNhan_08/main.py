from fastapi import FastAPI
from database import engine, Base
from models.category import CategoryModel
from models.dish import DishModel
from routers.dish import router as dish_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(dish_router)


@app.get("/")
def root():
    return {
        "statusCode": 200,
        "error": None,
        "message": "Trang chủ API Quản lý Món ăn",
        "data": None
    }