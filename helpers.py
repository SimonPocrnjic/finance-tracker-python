import datetime

def convert_date(strdate: str, format: str) -> str:
    if format == "yyyy-mm-dd":
        return strdate
    
    day: int = 0
    month: int = 0
    year: int = 0
    
    if format == "dd.mm.yyyy":
        split_str_date = strdate.split(".")
        day = int(split_str_date[0])
        month = int(split_str_date[1])
        year = int(split_str_date[2])
    
    return  datetime.date(
        year,
        month,
        day
    ).strftime("%Y-%m-%d")
    
def convert_amount(amount_str: str, tho_sep: str = ",", dec_sep: str = ".") -> float:
    return float(amount_str.replace(tho_sep, "").replace(dec_sep, "."))