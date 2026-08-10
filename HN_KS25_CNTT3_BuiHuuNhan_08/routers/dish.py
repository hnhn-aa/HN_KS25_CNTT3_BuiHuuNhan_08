from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database import get_db
from schemas.dish import DishUpdate
from services.dish import (
    get_all_dishes_service,
    update_dish_service,
    delete_dish_service
)

router = APIRouter(prefix="/dishes", tags=["Dishes Management"])


def build_response(status_code: int, message: str, data=None, error=None):
    return JSONResponse(
        status_code=status_code,
        content={
            "statusCode": status_code,
            "error": error,
            "message": message,
            "data": data
        }
    )


@router.get("/")
def get_all_dishes(db: Session = Depends(get_db)):
    data = get_all_dishes_service(db)
    return build_response(
        status_code=200,
        message="Lấy danh sách món ăn thành công",
        data=data
    )


@router.put("/{dish_id}")
def update_dish(dish_id: int, payload: DishUpdate, db: Session = Depends(get_db)):
    result = update_dish_service(db, dish_id, payload)
    
    if "error" in result:
        err_type = result["error"]
        if err_type == "dish_not_found":
            return build_response(
                status_code=404,
                error="Not Found",
                message="Món ăn không tồn tại"
            )
        elif err_type == "category_not_found":
            return build_response(
                status_code=404,
                error="Not Found",
                message="Danh mục không tồn tại"
            )
        elif err_type == "name_exists":
            return build_response(
                status_code=400,
                error="Bad Request",
                message="Tên món ăn đã tồn tại"
            )

    return build_response(
        status_code=200,
        message="Cập nhật thông tin món ăn thành công",
        data=result["data"]
    )


@router.delete("/{dish_id}")
def delete_dish(dish_id: int, db: Session = Depends(get_db)):
    success = delete_dish_service(db, dish_id)
    if not success:
        return build_response(
            status_code=404,
            error="Not Found",
            message="Món ăn không tồn tại"
        )

    return build_response(
        status_code=200,
        message="Xóa món ăn thành công",
        data=None
    )