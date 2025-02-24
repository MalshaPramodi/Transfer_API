from fastapi import FastAPI, HTTPException
from models.account import Account
from models.transaction import Transaction
from data.accounts_data import accounts  # Import accounts from the separate file

app = FastAPI()


@app.post("/transfer")
def transfer_funds(request: Transaction):
    source = accounts.get(request.source_account)
    destination = accounts.get(request.destination_account)

    if not source or not destination:
        raise HTTPException(status_code=404, detail="Account not found")

    # Ensure the transfer amount is positive
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Transfer amount must be greater than zero")

    # Ensure source account has enough balance
    if source["balance"] < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # Perform transfer
    source["balance"] -= request.amount
    destination["balance"] += request.amount

    return {
        "message": "Transfer successful",
        "source_balance": source["balance"],
        "destination_balance": destination["balance"]
    }
