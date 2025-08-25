def tax_calculator(subtotal, tax_rate=0.125):
    """
    Takes in subtotal and tax rate then returns
    [subtotal, tax, total]
    
    -Args:
    subtotal(float, int): cost of items in transactions
    tax_rate(float, optional): tax rate at store location
    (default is 0.125)
    
    -Returns:
    list: a list containing subtotal, tax and total
    """
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)
    
    return [subtotal, tax, total]
