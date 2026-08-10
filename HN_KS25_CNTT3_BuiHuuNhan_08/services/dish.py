from models.dish import DishModel
from models.category import CategoryModel
from sqlalchemy.orm import joinedload

def get_all_dishes_service(db):
    dishes = db.query(DishModel).options(joinedload(DishModel.category)).all()
    result_data = []
    for dish in dishes:
        result_data.append({
            "id": dish.id,
            "name": dish.name,
            "price": dish.price,
            "category": {
                "id": dish.category.id,
                "name": dish.category.name
            }
        })
    return result_data

def update_dish_service(db, dish_id, payload):
    dish = db.query(DishModel).filter(DishModel.id == dish_id).first()
    if not dish:
        return {"error": "dish_not_found"}

    category = db.query(CategoryModel).filter(CategoryModel.id == payload.category_id).first()
    if not category:
        return {"error": "category_not_found"}

    existing_name = db.query(DishModel).filter(
        DishModel.name == payload.name,
        DishModel.id != dish_id
    ).first()
    if existing_name:
        return {"error": "name_exists"}

    dish.name = payload.name
    dish.price = payload.price
    dish.category_id = payload.category_id

    db.commit()
    db.refresh(dish)

    return {
        "data": {
            "id": dish.id,
            "name": dish.name,
            "price": dish.price,
            "category": {
                "id": category.id,
                "name": category.name
            }
        }
    }

def delete_dish_service(db, dish_id):
    dish = db.query(DishModel).filter(DishModel.id == dish_id).first()
    if not dish:
        return False

    db.delete(dish)
    db.commit()
    return True