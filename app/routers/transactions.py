from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

get_db = database.get_db

@router.get("/", response_model=List[schemas.TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    # SELECT * FROM transactions;
    return db.query(models.Transaction).all()

@router.post("/", response_model=schemas.TransactionResponse)
def create_transaction(transaction: schemas.TransactionBase, db: Session = Depends(get_db)):
    
    new_transaction = models.Transaction(
        amount=transaction.amount,
        category=transaction.category,
        description=transaction.description
    )

    db.add(new_transaction)

    db.commit()

    db.refresh(new_transaction)

    return new_transaction