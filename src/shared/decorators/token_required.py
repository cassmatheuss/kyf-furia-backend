from functools import wraps
from flask import request, jsonify
from src.shared.utils.verify_token import verify_jwt_token

def jwt_required(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"message": "Token ausente"}), 401
        token = auth_header.split(' ')[1]
        try:
            verify = verify_jwt_token(token=token)
            if verify is None:
                raise Exception("Token inválido ou expirado")
        except Exception:
            return jsonify({"message": "Token inválido ou expirado"}), 401
        return fn(*args, **kwargs)
    return decorator
