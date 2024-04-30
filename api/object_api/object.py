from fastapi import APIRouter
from pydantic import BaseModel
from database.objectservice import (register_object_db, check_object_db,
                                    delete_object_db, change_obj_data)
obj_router = APIRouter()


# Модель объекта
class Object(BaseModel):
    game_id: int
    obj_name: str
    obj_rarity: str
    obj_price: int
    obj_type: str



# Создание новой вещи
@obj_router.post("/object/")
async def create_object(object_model: Object):
    object_data = dict(object_model)
    new_object = register_object_db(**object_data)
    if new_object:
        return {'status': 1,
                "message": "Предмет успешно добавлен"}
    return {'status':0, 'message': 'не получилось'}

# полученние денных о вещи по внутреигровому айди
@obj_router.get("/object/")
async def get_object(obj_name: str):
    exact_user = check_object_db(obj_name=obj_name)
    return {"status": 1, "message": exact_user}


# запрос на изменение информации о предмете
@obj_router.put("/api/change_object/")
async def change_object(object_id: int, changeable_info: str, new_data: str):
    data = change_obj_data(object_id=object_id,
                            changeable_info=changeable_info, new_data=new_data)
    return {"status": 1, "message": data}

@obj_router.delete("/object/")
async def delete_object(object_id: int):
    deleted = delete_object_db(object_id)
    if deleted:
        return {'status': 1,
                "message": "Объект успешно удален"}
    return {'status': 0, 'message': 'Не удалось удалить объект'}