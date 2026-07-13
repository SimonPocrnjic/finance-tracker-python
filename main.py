from pathlib import Path
from constants import PATH_TO_STORAGE
from models import Transaction
from storage import load_all, overwrite_all
from importer import import_csv

ACTIONS: list[str] = [
    "import_bank_csv"
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
    
    imported_list: list[Transaction] = import_csv(csv_path, existing_ids)
    new_list = existing_list + imported_list
    overwrite_all(PATH_TO_STORAGE, new_list)
    print("\n### Import finished ###")
    

def main():
    print("---------Start program-------------\n")
    print("List of actions:")
    choose_action()
    
    while True:
        action = input("Enter between 0-1 (type 'h' for list): ")
        if action == '0':
            break
        
        if action == '1':
            import_bank_csv()
        elif action == 'h':
            choose_action()
        else:
            print("Not found, choose from list below!")
            choose_action()
            
    print("\n---------Closing program-------------")
            

main()