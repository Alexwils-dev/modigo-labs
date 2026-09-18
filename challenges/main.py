def to_roman(number):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""

    for value, symbol in zip(values, symbols):
        count = number // value
        result += symbol * count
        number = number % value

    return result
print(to_roman(14))