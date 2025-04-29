from flask import Blueprint, request

from src.modules.signup.signup_repository import SignupRepository
from src.modules.signup.signup_usecase import SignupUseCase

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    repository = SignupRepository()
    usecase = SignupUseCase(repository)
    result = usecase(data)
    status_code = 200
    return result, status_code