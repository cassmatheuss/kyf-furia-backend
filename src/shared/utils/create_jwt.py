import os
import jwt
import datetime

SECRET_KEY = os.getenv("JWT_SECRET")

def create_jwt_token(data: dict, expires_in: int = 3600):
    payload = data.copy()
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")