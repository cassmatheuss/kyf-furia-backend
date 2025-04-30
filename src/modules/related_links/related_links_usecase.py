from src.modules.signin.signin_viewmodel import SigninViewModel
from src.shared.utils.create_jwt import create_jwt_token
from src.modules.signin.signin_repository import SigninRepository

class RelatedLinksUseCase:
    def __init__(self, repo: SigninRepository):
        self.repo = repo

    def __call__(self, data: dict):
        try:
            email = data.get("email")
            password = data.get("password")
            user = self.repo.authenticate_user(email, password)
            if not user:
                raise ValueError("Usuário não encontrado.")
            viemodel = SigninViewModel(token=create_jwt_token(data={"email": user["email"], "sub": str(user["_id"]), "resume": user["resume"]}))
            return viemodel.dict()
        except Exception as e:
            raise Exception(f"{str(e)}")
