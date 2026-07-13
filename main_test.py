import hashlib
import traceback
import json
import random
import datetime
from models import Transaction
from storage import load_all, append
from constants import PATH_TO_TEST_STORAGE
from importer import computed_id, import_csv

available_tests: list[str] = [
    "test_transaction_creation",
    "test_storage",
    "test_computed_id",
    "test_importer"
]

def main_test():
    print("--------------Start tests--------------")
    print("Choose test to run:")
    choose_test()
    
    while True:
        data = input("Enter test to run:\n")
        if 'exit' == data:
            break
        if data == '1':
            test_transaction_creation()
        elif data == '2':
            test_storage()
        elif data == '3':
            test_computed_id()
        elif data == '4':
            test_importer()
        else:
            print("Not found, choose from list below!")
            choose_test()
            
    print("--------------Finished testing--------------")


"Test functions"

def test_transaction_creation() -> None:
    print("### Start transaction creation test ###\n")
    try:
        test_transaction = create_transaction()
        expected_result = "{\"id\": \"dwdwggggdwdddd\", \"date\": \"2026-12-04\", \"amount\": 40.31, \"category\": \"debit\", \"description\": \"Electricity\", \"account\": \"My account\"}"
        actual_result = json.dumps(test_transaction.to_dict())
        print(f"Expected: {expected_result}")
        print(f"Actual: {actual_result}")
        if (expected_result == actual_result):
            print("pass")
        else:
            print("failed")
    except Exception as e:
        print(f"Something went wrong creating transaction: {str(e)}")
    
    print("\n### Creating transaction test finished ###")

def test_storage() -> None:
    print("### Start storage test ###")
    try:
        test_transaction = create_transaction()
        append(PATH_TO_TEST_STORAGE, test_transaction)
        print(f"Written line to {PATH_TO_TEST_STORAGE}: {json.dumps(test_transaction.to_dict())}\n")
        expected_result = "{\"id\": \"dwdwggggdwdddd\", \"date\": \"2026-12-04\", \"amount\": 40.31, \"category\": \"debit\", \"description\": \"Electricity\", \"account\": \"My account\"}"
        actual_result: str = None
        
        "Read written line from file"
        with open(PATH_TO_TEST_STORAGE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                actual_result = line
                break
        
        print(f"Expected: {expected_result}")
        print(f"Actual: {actual_result}")
        if (expected_result == actual_result):
            print("pass")
        else:
            print("failed")
       
    except Exception as e:
        print(f"Something went wrong writting to file: {str(e)}")
        
    with open(PATH_TO_TEST_STORAGE, "w") as f:
        f.write("")
        f.close()
    
    print("\n### Storage test finished ###")
    
def test_computed_id() -> None:
    print("### Start generate computed id test ###\n")
    try:
        "Test is equal hash"
        test_data: tuple[str,float,str] = ("2026-06-13", 30.52, "Some description")
        key = f"{test_data[0]}-{str(test_data[1])}-{test_data[2]}".encode()
        compare_hash = hashlib.sha256(key).hexdigest()[:12]
        gen_hash = computed_id(test_data[0], test_data[1], test_data[2])
        
        if gen_hash == compare_hash:
            print(f"Compare hash {compare_hash} is equal to {gen_hash}.")
        else:
            print(f"Compare hash {compare_hash} is not equal to {gen_hash}. Test failed!")
            
        "Test is not equal hash"
        key = f"2026-05-13-{str(23.55)}-Other description".encode()
        compare_hash = hashlib.sha256(key).hexdigest()[:12]
        
        if gen_hash != compare_hash:
            print(f"Compare hash {compare_hash} is not equal to {gen_hash}.")
        else:
            print(f"Compare hash {compare_hash} is equal to {gen_hash}. Test failed!")
    except Exception as e:
        print(f"Something went wrong generating computed id: {str(e)}")
    print("\n### Computed id test finished ###")
    
def test_importer() -> None:
    print("### Start import test ###\n")
    try: 
        test_transactions: list[Transaction] = import_csv("TEST_BANK_DATA.csv", set())
        print(json.dumps(test_transactions[0].to_dict()))
    except Exception as e:
        print(f"Something went wrong importing csv: {traceback.format_exc()}")
    
    print("\n### Import test finished ###")

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
    
def choose_test() -> None:
    for i in range(0, len(available_tests)):
        print(f"{i+1}: {available_tests[i]}")
    print("Close program: exit\n")
        
main_test()