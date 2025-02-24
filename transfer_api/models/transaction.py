from pydantic import BaseModel

class Transaction(BaseModel):
    source_account: str
    destination_account: str
    amount: float
