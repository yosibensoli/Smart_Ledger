from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database, auth  

router = APIRouter()


@router.get("/", response_model=List[schemas.TransactionResponse])
def get_transactions(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user) 
):
    
    return db.query(models.Transaction).filter(models.Transaction.user_id == current_user.id).all()

@router.post("/", response_model=schemas.TransactionResponse)
def create_transaction(
    transaction: schemas.TransactionCreate, 
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user) 
):
    new_transaction = models.Transaction(
        amount=transaction.amount,
        category=transaction.category,
        description=transaction.description,
        user_id=current_user.id
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction