from pydantic import BaseModel

class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str | None = None

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int  

    class Config:
        from_attributes = True