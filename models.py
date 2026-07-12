from dataclasses import dataclass

@dataclass
class Transaction:
    id: str
    date: str
    amount: float
    category: str
    description: str
    account: str
    
    def to_dict(self) -> dict:
        return self.__dict__
    
    @classmethod
    def from_dict(cls, data: dict) -> "Transaction":
        return cls(**data)