
def tax_calculator(subtotal: float, tax_rate: float) -> float:
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)
    
    return [subtotal, tax, total]
