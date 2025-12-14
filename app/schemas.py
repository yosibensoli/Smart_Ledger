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


class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True