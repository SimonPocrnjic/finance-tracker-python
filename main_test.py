import json
import random
import datetime
from models import Transaction
from storage import load_all, append


def main_test() -> None:
    print("--------------Start tests--------------")
    test_transaction_creation()
    print("--------------Finished testing--------------")


"Test functions"

def test_transaction_creation() -> None:
    print("### Start transaction creation test ###")
    try:
        test_transaction = create_transaction()
        print(json.dumps(test_transaction.to_dict()))
    except Exception as e:
        print(f"Something went wrong creating transaction {str(e)}")
    
    print("### Creating transaction test finished ###")

def test_storage() -> None:
    print("### Start storage test ###")
    print("### Storage test finished ###")

"Helper function"    

def create_transaction() -> Transaction:
    return Transaction(
        "dwdwggggdwdddd",
        f"{datetime.date(2026,12,4).strftime("%Y-%m-%d")}",
        40.31,
        "debit",
        "Electricity",
        "My account"
    )
        
        
main_test()