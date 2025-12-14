from fastapi import FastAPI
from app.routers import transactions
from app.database import engine
from app import models           

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "SmartLedger API is running"}

app.include_router(
    transactions.router,
    prefix="/transactions", 
    tags=["Transactions"]  
)