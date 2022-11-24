from pydantic import BaseModel

class passwordForm(BaseModel):
    name: str
    password: str

class groupForm(BaseModel):
    name: str