from pydantic import BaseModel

class Payload(BaseModel):
    user_input: str

class PayloadData(BaseModel):
    user_input: str