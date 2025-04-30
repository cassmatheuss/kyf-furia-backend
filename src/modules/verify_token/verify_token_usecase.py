from src.modules.verify_token.verify_token_repository import VerifyTokenRepository
from src.modules.verify_token.verify_token_viewmodel import VerifyTokenViewModel
from src.shared.utils.face_validation import compare_faces_base64
from src.modules.signup.signup_repository import SignupRepository
from src.modules.signup.signup_viewmodel import SignupViewModel
from src.shared.entities.User import User

class VerifyTokenUseCase:
    def __init__(self, repo: VerifyTokenRepository):
        self.repo = repo

    def __call__(self, data: dict):
        try:
            token = data.get('token')
            verification = self.repo.verify_token(token)
            isOk = verification
            
            if not isOk:
                return VerifyTokenViewModel(valid=False).dict()
                
            return VerifyTokenViewModel(valid=isOk).dict()
            
            
        except Exception as e:
            raise Exception(f"Erro ao processar o VerifyTokenUseCase: {str(e)}")
