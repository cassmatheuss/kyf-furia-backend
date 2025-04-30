from pydantic import BaseModel

class SigninViewModel(BaseModel):
    token: str