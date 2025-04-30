
from src.shared.utils.verify_token import verify_jwt_token

class VerifyTokenRepository:
    def verify_token(self, token):
        verification = verify_jwt_token(token)
        if verification is None:
            return False
        else:
            return True