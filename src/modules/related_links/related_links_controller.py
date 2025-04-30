from flask import Blueprint, request
from src.modules.signin.signin_repository import SigninRepository
from src.modules.signin.signin_usecase import SigninUseCase

related_links_bp = Blueprint('related-links', __name__)

@related_links_bp.route('/related-links', methods=['GET'])
def related_links():

    repository = RelatedLinksRepository()
    usecase = RelatedLinksUseCase(repository)
    data = {
        "email": request.args.get('email'),
        "password": request.args.get('password')
    }

    try:
        result = usecase(data)
        status_code = 200
    except Exception as e:
        result = {"error": str(e)}
        status_code = 401
    return result, status_code
