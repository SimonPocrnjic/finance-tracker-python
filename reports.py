import json
from collections import defaultdict
from models import Transaction

def monthly_summary(transactions: list[Transaction], month: str) -> dict:
    filtered = [t for t in transactions if t.date.startswith(month)]
    summary = defaultdict(float)
    for t in filtered:
        print(json.dumps(t.to_dict()))
        summary[t.category] += t.amount
        
    return summary

def totals(summary: dict) -> tuple[float, float]:
    income = 0.0
    expenses = 0.0
    
    for amount in summary.values():
        if amount > 0:
            income += amount
        elif amount < 0:
            expenses += amount
    
    return income, expenses

def print_summary(summary: dict) -> None:
    sorted_items = sorted(summary.items(), key=lambda item: abs(item[1]), reverse=True)
    
    print(f"{'Category':<20}{'Amount':>10}")
    print("-" * 30)
    for category, amount in sorted_items:
        print(f"{category:<20}{amount:>10.2f}")
    
    income, expenses = totals(summary)
    print("-" * 30)
    print(f"{'Income':<20}{income:>10.2f}")
    print(f"{'Expenses':<20}{expenses:>10.2f}")
    print(f"{'Net':<20}{income + expenses:>10.2f}")