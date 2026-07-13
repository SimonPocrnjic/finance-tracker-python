from pathlib import Path
from constants import PATH_TO_STORAGE
from models import Transaction
from storage import load_all, overwrite_all
from importer import import_csv
from categorizer import load_rules, categorize, overwrite_rules

ACTIONS: list[str] = [
    "import_bank_csv",
    "categorize_transactions"
]

def choose_action() -> None:
    for i in range(0, len(ACTIONS)):
        print(f"{i+1}: {ACTIONS[i]}")
    print("0: Close program\n")
    
def import_bank_csv() -> None:
    print("### Import csv ###\n")
    csv_path = input("Path to csv file: ")
    csv_path = Path(csv_path)
    
    if not csv_path.exists():
        print("File was not found!")
        return
    
    existing_list: list[Transaction] = load_all(PATH_TO_STORAGE)
    existing_ids: set[str] = set()
    for t in existing_list:
        existing_ids.add(t.id)
    
    rules = load_rules("rules.json")
    imported_list: list[Transaction] = import_csv(csv_path, existing_ids, rules)
    new_list = existing_list + imported_list
    overwrite_all(PATH_TO_STORAGE, new_list)
    print("\n### Import finished ###")
    
def categorize_transactions() -> None:
    print("### Start categorizing  ###\n")
    rules = load_rules("rules.json")
    
    category = input("Enter new category (exit 'x' or '0'): ")
    
    for rule in rules:
        if category == rules[rule]:
            category = input("Enter a category that does not yet exist (exit 'x' or '0'): ")
            break
    if category == "x" or category == "0":
        return
    
    keyword = input("Enter unique keyword (exit 'x' or '0'): ")
    for rule in rules.keys():
        if keyword.upper() == rule:
            keyword = input("Enter a keyword that does not yet exist (exit 'x' or '0'): ")
            break
    if keyword == "x" or category == "0":
        return
    
    rules[keyword] = category
    overwrite_rules("rules.json", rules)
    
    transactions = load_all(PATH_TO_STORAGE)
    for t in transactions:
        if t.category == "Uncategorized":
            result = categorize(t.description, rules)
            if result:
                t.category = result
            
    overwrite_all(PATH_TO_STORAGE, transactions)
    print("Transactions saved.")
    print("\n### Finished categorize  ###")

def main():
    print("---------Start program-------------\n")
    print("List of actions:")
    choose_action()
    
    while True:
        action = input("Enter between 0-2 (type 'h' for list): ")
        if action == '0':
            break

        if action == '1':
            import_bank_csv()
        elif action == '2':
            categorize_transactions()
        elif action == 'h':
            choose_action()
        else:
            print("Not found, choose from list below!")
            choose_action()
            
    print("\n---------Closing program-------------")
            

main()