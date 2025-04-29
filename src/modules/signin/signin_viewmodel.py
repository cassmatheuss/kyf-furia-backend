from pydantic import BaseModel

class SignupViewModel(BaseModel):
    message: str