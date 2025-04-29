import os
import bcrypt
from langchain_openai import ChatOpenAI
from src.shared.utils.mongo_connect import connect_mongodb
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class SignupRepository:
    def __init__(self):
        self.db = connect_mongodb(
            url=os.getenv("MONGO_DB_URL"),
            db_name=os.getenv("DB_NAME")
        )
        self.llm = ChatOpenAI(
            model="openai/gpt-4o-mini",
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base=os.getenv("OPENROUTER_BASE_URL"),
        )

    def make_resume(self, user):
        user_data = (
            f"Nome: {user.name}\n"
            f"Email: {user.email}\n"
            f"Telefone: {user.phone}\n"
            f"Data de nascimento: {user.birth_date}\n"
            f"Endereço: {user.address}\n"
            f"Interesses: {user.interests}\n"
            f"Atividades: {user.activities}\n"
            f"Eventos: {user.events}\n"
            f"Compras no ultimo ano: {user.purchases}\n"
            f"Instagram: {user.instagram}\n"
            f"Twitter: {user.twitter}"
        )

        prompt = PromptTemplate(
            template=(
                "Com base nos dados abaixo, gere um resumo objetivo (até 300 caracteres) sobre o perfil e preferências deste usuário, focando em interesses e atividades. Pode tomar como base tambem as compras dele:\n\n{user_data}"
            ),
            input_variables=["user_data"]
        )
        chain = LLMChain(prompt=prompt, llm=self.llm)
        resume = chain.run({"user_data": user_data})
        return resume[:400]

    def create_user(self, user):
        if self.db.users.find_one({"email": user.email}):
            raise ValueError("E-mail já cadastrado.")

        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        user_dict = user.dict()
        user_dict['password'] = hashed_password.decode('utf-8')
        user_dict['resume'] = self.make_resume(user)

        result = self.db.users.insert_one(user_dict)
        return result.inserted_id
