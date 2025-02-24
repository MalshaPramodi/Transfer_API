from pydantic import BaseModel

class Account(BaseModel):
    account_number: str
    balance: float
