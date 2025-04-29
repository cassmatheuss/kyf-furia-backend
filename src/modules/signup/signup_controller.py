from flask import Blueprint, request
from src.modules.signup.signup_repository import SignupRepository
from src.modules.signup.signup_usecase import SignupUseCase
import base64

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['POST'])
def signup():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")
    birth_date = request.form.get("birth_date")
    address = request.form.get("address")
    interests = request.form.get("interests")
    activities = request.form.get("activities")
    events = request.form.get("events")
    purchases = request.form.get("purchases")
    instagram = request.form.get("instagram", "")
    twitter = request.form.get("twitter", "")
    document_file = request.files.get("document")
    user_image_file = request.files.get("user_image")

    def file_to_base64(file):
        if not file:
            return ""
        b64 = base64.b64encode(file.read()).decode()
        return f"data:image/jpeg;base64,{b64}"

    document_b64 = file_to_base64(document_file)
    user_image_b64 = file_to_base64(user_image_file)

    data = {
        "name": name,
        "email": email,
        "password": password,
        "phone": phone,
        "birth_date": birth_date,
        "address": address,
        "interests": interests,
        "activities": activities,
        "events": events,
        "purchases": purchases,
        "instagram": instagram,
        "twitter": twitter,
        "document": document_b64,
        "user_image": user_image_b64,
    }

    repository = SignupRepository()
    usecase = SignupUseCase(repository)
    result = usecase(data)
    status_code = 200
    return result, status_code
