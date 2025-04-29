from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    birth_date: str
    address: str
    interests: str
    activities: str
    events: str
    purchases: str
    instagram: str = ""
    twitter: str = ""
    resume: str = ""
    document: str
    user_image: str
