import json
from pathlib import Path
from models import Transaction

def load_all(path: str) -> list[Transaction]:
    p = Path(path)
    
    if not p.exists():
        return []

    transactions: list[Transaction] = []
    
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            transactions.append(Transaction.from_dict(data))
    return transactions

def append(path: str, transaction: Transaction) -> None:
    p = Path(path) 
    
    with open(p, "a") as f:
            f.write(json.dumps(transaction.to_dict()) + "\n")

def overwrite_all(path: str, transactions: list[Transaction]) -> None:
    p = Path(path)
    
    with open(p, "w") as f:
        for t in transactions:
            f.write(json.dumps(t.to_dict()) + "\n")
    