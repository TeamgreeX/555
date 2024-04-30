from database import get_db
from database.models import Type

# добавление типа
def add_type_db(text):
    db = next(get_db())
    new_type = Type(text=text)
    db.add(new_type)
    db.commit()
    return new_type.id

# чекер типа
def check_type_db(type_id):
    db = next(get_db())
    checker = db.query(Type).filter_by(type_id=type_id).first()
    if checker:
        return False
    return True

# изменение типа вещи
def change_type_data(type_id, changeable_info, new_data):
    db = next(get_db())
    all_info = db.query(Type).filter_by(id=type_id).first()
    if all_info:
        if changeable_info == "text":
            all_info.text = new_data
        db.commit()
        return "Данные успешно изменены"
    return "Тип не найден"

# удаление типа вещи
def delete_type_db(type_id):
    db = next(get_db())
    try:
        delete = db.query(Type).filter_by(type_id=type_id).delete()
        db.commit()
        return delete
    except Exception as e:
        return 'данный ID не существует'
