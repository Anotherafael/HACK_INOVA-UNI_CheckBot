from pydantic import BaseModel

class Payload(BaseModel):
    user_input: str