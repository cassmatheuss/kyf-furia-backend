from pydantic import BaseModel

class VerifyTokenViewModel(BaseModel):
    valid: bool