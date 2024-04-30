from fastapi import FastAPI
from database import Base, engine
from api.object_api.object import obj_router
from api.user_api.user import user_router
from api.type_api.type import tp_router
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/')
app.include_router(user_router)
app.include_router(obj_router)
app.include_router(tp_router)
