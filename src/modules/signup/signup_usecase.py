from src.shared.utils.face_validation import compare_faces_base64
from src.modules.signup.signup_repository import SignupRepository
from src.modules.signup.signup_viewmodel import SignupViewModel
from src.shared.entities.User import User

class SignupUseCase:
    def __init__(self, repo: SignupRepository):
        self.repo = repo

    def __call__(self, data: dict):
        try:
            document_b64 = data.get("document")
            user_image_b64 = data.get("user_image")

            if not compare_faces_base64(document_b64, user_image_b64):
                raise Exception("As imagens não correspondem à mesma pessoa. Cadastro não permitido.")

            user = User(
                name=data.get("name"),
                email=data.get("email"),
                password=data.get("password"),
                phone=data.get("phone"),
                birth_date=data.get("birth_date"),
                address=data.get("address"),
                interests=data.get("interests"),
                activities=data.get("activities"),
                events=data.get("events"),
                purchases=data.get("purchases"),
                instagram=data.get("instagram", ""),
                twitter=data.get("twitter", ""),
                resume="",
                document=document_b64,
                user_image=user_image_b64,
            )

            self.repo.create_user(user)
            return SignupViewModel(
                message=f"Usuário {data.get('name')} criado com sucesso",
            ).dict()
        except Exception as e:
            raise Exception(f"Erro ao processar o SignupUseCase: {str(e)}")
