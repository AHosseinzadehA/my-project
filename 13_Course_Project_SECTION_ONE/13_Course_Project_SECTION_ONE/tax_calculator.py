
def tax_calculator(subtotal, tax_rate=1.07):
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)

    return [subtotal, tax, total]
