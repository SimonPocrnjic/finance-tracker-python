import json
from pathlib import Path

def categorize(description: str, rules: dict[str, str]) -> str | None:
    found_desc = None
    
    for rule in rules:
        if rule in  description.upper():
            found_desc = rules[rule]
            break
    return found_desc
        
    
def load_rules(path: str) -> dict[str, str]:
    p = Path(path)
    
    if not p.exists():
        return {}
    
    data: dict[str, str] = {}
    with open(p, encoding="utf-8") as f:
        data = json.load(f)
        
    return data

def overwrite_rules(path: str, rules: dict[str, str]) -> None:
    p = Path(path)
    
    with open(p, "w") as f:
        json.dump(rules, f)