from datetime import datetime
import pandas as pd
import re

def split_price(price_str):
    match = re.match(r"([0-9.,]+)(\D+)", price_str)
    if match:
        amount, currency = match.groups()
        amount = amount.replace(",", ".") 
        return {"currency": currency.strip(), "amount": amount}
    else:
        return {"currency": "", "amount": price_str}
    
def transform_date(date_str):
    try:
        return datetime.strptime(date_str, "%b %d, %Y").strftime("%Y-%m-%d")
    except ValueError:
        return date_str  

def extract_digits(text):
    return re.sub(r"[^\d]", "", text)

transformations = {
    "text": lambda element: element.text() if element else None,
    "attr": lambda element, attr: element.attributes.get(attr) if element else None,
    "split_price": lambda node: split_price(node.text()),
    "date_format": lambda date_str: transform_date(date_str),
    "digit_only": lambda node: extract_digits(node.text()),
}

def apply_transformation(value, transformation, *args):
    if transformation in transformations:
        if transformation == "attr":
            return transformations[transformation](value, args[0]) 
        return transformations[transformation](value, *args)  
    return value



def save_to_file(filename="extract.csv",data: list[dict] = None):
    if data is None:
        raise ValueError("The function expects data to be provided as a list of dict.")
    df = pd.DataFrame(data)
    filename = f"{datetime.now().strftime('%Y_%m_%d')}_{filename}.csv"
    df.to_csv(filename, index=False)