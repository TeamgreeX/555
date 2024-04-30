from sqlalchemy import (Column, Integer, String,
                        DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)
    reg_date = Column(DateTime)


class Type(Base):
    __tablename__ = "type_object"
    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(String, nullable=False)


class Object(Base):
    __tablename__ = "object"
    id = Column(Integer, autoincrement=True, primary_key=True)
    game_id = Column(Integer, unique=True)
    obj_name = Column(String, unique=True)
    obj_rarity = Column(String, nullable=False)
    obj_price = Column(Integer, nullable=False)
    obj_type = Column(Integer, ForeignKey('type_object.id'))
    type_fk = relationship(Type, lazy="subquery")
