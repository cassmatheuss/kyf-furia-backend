from pydantic import BaseModel

class RelatedLinksViewModel(BaseModel):
    score: int
    text: str