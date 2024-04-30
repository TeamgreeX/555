from fastapi import APIRouter
from pydantic import BaseModel
from database.typeservice import (add_type_db, check_type_db, change_type_data, delete_type_db)
tp_router = APIRouter()


# Модель типа
class Type(BaseModel):
    text: str



# Создание новой вещи
@tp_router.post("/type/")
async def create_object(type_model: Type):
    type_data = dict(type_model)
    new_type = add_type_db(**type_data)
    if new_type:
        return {'status': 1,
                "message": "Предмет успешно добавлен"}
    return {'status':0, 'message': 'не получилось'}

# полученние денных о вещи по внутреигровому айди
@tp_router.get("/type/")
async def get_type(type_id: int):
    exact_type = check_type_db(type_id=type_id)
    return {"status": 1, "message": exact_type}


# запрос на изменение информации о предмете
@tp_router.put("/api/change_type/")
async def change_type(type_id: int, changeable_info: str, new_data: str):
    data = change_type_data(type_id=type_id,
                            changeable_info=changeable_info, new_data=new_data)
    return {"status": 1, "message": data}

@tp_router.delete("/type/")
async def delete_type(type_id: int):
    deleted = delete_type_db(type_id)
    if deleted:
        return {'status': 1,
                "message": "Объект успешно удален"}
    return {'status': 0, 'message': 'Не удалось удалить объект'}