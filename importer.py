import hashlib
import csv
from models import Transaction
from constants import DEFAULT_CSV_DELIMENTOR, CSV_COLUMN_MAPPER, DEFAULT_DECIMAL_SEPARATOR, DEFAULT_THOUSAND_SEPARATOR, DEFAULT_DATE_FORMAT
from helpers import convert_date, convert_amount
from categorizer import categorize

def computed_id(date: str, amount: float, description: str) -> str:
    unique_key = f"{date}-{amount}-{description}".encode()
    return hashlib.sha256(unique_key).hexdigest()[:12]

def import_csv(csv_path: str, existing_ids: set[str], rules: dict[str, str] = {}) -> list[Transaction]:
    transaction_list: list[Transaction] = []
    with open(csv_path, encoding="utf-8") as f:
        data = csv.DictReader(f, delimiter=DEFAULT_CSV_DELIMENTOR) 
        for row in data:
            amount: float = 0.00
            flow: str = "debit"
            
            if row[CSV_COLUMN_MAPPER["debit"]] != "" and row.get(CSV_COLUMN_MAPPER["debit"]) != None:
                amount = convert_amount(row[CSV_COLUMN_MAPPER["debit"]], DEFAULT_THOUSAND_SEPARATOR, DEFAULT_DECIMAL_SEPARATOR) * -1
            elif row[CSV_COLUMN_MAPPER["credit"]] != "" and row.get(CSV_COLUMN_MAPPER["debit"]) != None:
                amount = convert_amount(row[CSV_COLUMN_MAPPER["credit"]], DEFAULT_THOUSAND_SEPARATOR, DEFAULT_DECIMAL_SEPARATOR)
                flow = "credit"
            elif row[CSV_COLUMN_MAPPER["amount"]] != "" and row.get(CSV_COLUMN_MAPPER["amount"]) != None:
                amount = convert_amount(row[CSV_COLUMN_MAPPER["amount"]], DEFAULT_THOUSAND_SEPARATOR, DEFAULT_DECIMAL_SEPARATOR)
                
            "TODO: other condition depending on the banks exported csv"
            
            description = f"number {row[CSV_COLUMN_MAPPER["nu"]]}, description {row[CSV_COLUMN_MAPPER["description"]]}, flow {flow}"
            new_id = computed_id(
                row[CSV_COLUMN_MAPPER["date"]],
                amount,
                description
            )
            
            if new_id in existing_ids:
                continue
            
            correct_date = convert_date(row[CSV_COLUMN_MAPPER["date"]], DEFAULT_DATE_FORMAT)
            transaction = Transaction(
                new_id,
                correct_date,
                amount,
                "Uncategorized",
                description,
                row[CSV_COLUMN_MAPPER["account"]]
            )
            
            category = categorize(transaction.description, rules)
            transaction.category = category or "Uncategorized"
            
            transaction_list.append(transaction)
            existing_ids.add(new_id)
        
    return transaction_list
        
