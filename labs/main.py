def format_line_item(description, amount, tax_rate=7.5, currency="$"):
    total = round(amount + (amount * tax_rate / 100), 2)
    return (f"{description}: {currency}{total}")
    
print(format_line_item("Notebook", 10))