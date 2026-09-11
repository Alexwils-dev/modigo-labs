def apply_discount(price, discount_percent=10):
    return round(price - (price * discount_percent / 100), 2)

print(apply_discount(100))