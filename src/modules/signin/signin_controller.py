from flask import Blueprint, request
from src.modules.signin.signin_repository import SigninRepository
from src.modules.signin.signin_usecase import SigninUseCase

signin_bp = Blueprint('signin', __name__)

@signin_bp.route('/signin', methods=['POST'])
def signin():
    email = request.form.get("email")
    password = request.form.get("password")

    data = {
        "email": email,
        "password": password,
    }

    repository = SigninRepository()
    usecase = SigninUseCase(repository)
    try:
        result = usecase(data)
        status_code = 200
    except Exception as e:
        result = {"error": str(e)}
        status_code = 401
    return result, status_code
