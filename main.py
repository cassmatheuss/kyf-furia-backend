from flask import Flask
from flask_cors import CORS

from src.shared.infra.Environments import Environments
from src.modules.signup.signup_controller import signup_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(signup_bp)

if __name__ == '__main__':
    Environments()
    app.run(debug=True)