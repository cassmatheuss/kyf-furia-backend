import os
from flask import Blueprint, request
import jwt
from src.shared.decorators.token_required import jwt_required
from src.modules.related_links.related_links_usecase import RelatedLinksUseCase
from src.modules.related_links.related_links_repository import RelatedLinksRepository


related_links_bp = Blueprint('related-links', __name__)

def get_resume_from_token(token):
    try:
        payload = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms=["HS256"])
        return payload.get('resume')
    except Exception as e:
        return None
    
@related_links_bp.route('/related-links', methods=['POST'])
@jwt_required
def related_links():

    repository = RelatedLinksRepository()
    usecase = RelatedLinksUseCase(repository)
    auth_header = request.headers.get('Authorization', None)
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
    else:
        token = None
    data = {
        "resume": get_resume_from_token(token),
        "site_url": request.form.get('site_url')
    }

    try:
        result = usecase(data)
        status_code = 200
    except Exception as e:
        result = {"error": str(e)}
        status_code = 401
    return result, status_code
