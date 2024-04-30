import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'BotirAka-Maladez-BotirAka-Horoshiy-BotirAka-Lubimiy'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTE = 300


# Наш JWT тут создает токен
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({'expires': expire.isoformat()})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


# провeрка токена
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        return 'Error'