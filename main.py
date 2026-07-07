from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import logging

# Initialize App
app = FastAPI(title="Automated Credit Management API", version="1.0.0")

# Setup Basic Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BankingAPI")

# Dummy Database
TRANSACTIONS_DB = []

# Pydantic Schemas
class CreditTransaction(BaseModel):
    account_number: str
    amount: float
    currency: str = "PKR"
    description: str

@app.get("/")
def read_root():
    return {"status": "Active", "system": "UBL Strategic Initiatives Mock API"}

@app.post("/api/v1/credit", response_model=CreditTransaction)
def create_credit_entry(transaction: CreditTransaction):
    if transaction.amount <= 0:
        logger.error(f"Failed credit attempt: Negative amount for account {transaction.account_number}")
        raise HTTPException(status_code=400, detail="Transaction amount must be greater than zero.")
    
    # Simulate DB Save
    TRANSACTIONS_DB.append(transaction)
    logger.info(f"Successful Credit: {transaction.amount} PKR to Account {transaction.account_number}")
    return transaction

@app.get("/api/v1/transactions", response_model=List[CreditTransaction])
def get_all_transactions():
    return TRANSACTIONS_DB
