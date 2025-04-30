from flask import Blueprint, request

from src.modules.verify_token.verify_token_repository import VerifyTokenRepository
from src.modules.verify_token.verify_token_usecase import VerifyTokenUseCase


verifytoken_bp = Blueprint('verifytoken', __name__)

@verifytoken_bp.route('/verifytoken', methods=['POST'])
def verifytoken():
    token = request.form.get("token")
    if not token:
        return {"error": "Token não fornecido."}, 400
    data = {
        "token": token
    }
    repository = VerifyTokenRepository()
    usecase = VerifyTokenUseCase(repository)
    result = usecase(data)
    status_code = 200
    return result, status_code
