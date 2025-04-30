import os
import bcrypt
from src.shared.utils.mongo_connect import connect_mongodb

class RelatedLinksRepository:
    def __init__(self):
        self.db = connect_mongodb(
            url=os.getenv("MONGO_DB_URL"),
            db_name=os.getenv("DB_NAME")
        )

    def authenticate_user(self, email, password):
        user = self.db.users.find_one({"email": email})
        if not user:
            raise ValueError("Usuário não encontrado.")

        hashed_password = user['password'].encode('utf-8')
        if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            raise ValueError("Senha incorreta.")

        return user