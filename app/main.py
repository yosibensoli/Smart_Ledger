from fastapi import FastAPI
from app.routers import transactions, users, auth  
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    transactions.router,
    prefix="/transactions",
    tags=["Transactions"]
)

app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    auth.router,
    tags=["Authentication"] 
)

@app.get("/")
def read_root():
    return {"message": "SmartLedger API is running"}