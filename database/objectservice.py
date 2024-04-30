from database import get_db
from database.models import Object

def register_object_db(obj_name, game_id, obj_rarity, obj_price, obj_type):
    db = next(get_db())
    new_object = Object(obj_name=obj_name, game_id=game_id, obj_rarity=obj_rarity, obj_price=obj_price, obj_type=obj_type)
    db.add(new_object)
    db.commit()
    return new_object.id

def check_object_db(obj_name):
    db = next(get_db())
    checker = db.query(Object).filter_by(obj_name=obj_name).first()
    if checker:
        return False
    return True

def change_obj_data(object_id, changeable_info, new_data):
    db = next(get_db())
    all_info = db.query(Object).filter_by(id=object_id).first()
    if all_info:
        if changeable_info == "game_id":
            all_info.game_id = new_data
        elif changeable_info == "obj_name":
            all_info.obj_name = new_data
        elif changeable_info == "obj_rarity":
            all_info.obj_rarity = new_data
        elif changeable_info == "obj_price":
            all_info.obj_price = new_data
        elif changeable_info == "obj_type":
            all_info.obj_type = new_data
        db.commit()
        return "Данные успешно изменены"
    return "Вещь не найдена"


def delete_object_db(game_id):
    db = next(get_db())
    try:
        delete = db.query(Object).filter_by(game_id=game_id).delete()
        db.commit()
        return delete
    except Exception as e:
        return 'данный ID не существует'
