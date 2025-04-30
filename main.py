import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from src.shared.infra.Environments import Environments
from src.modules.signup.signup_controller import signup_bp
from src.modules.signin.signin_controller import signin_bp
from src.modules.verify_token.verify_token_controller import verifytoken_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(signup_bp)
app.register_blueprint(signin_bp)
app.register_blueprint(verifytoken_bp)
if __name__ == '__main__':
    Environments()
    app.run(debug=True)