def sum_of_digits(number):
    total = 0
    number = str(number)

    for digit in number:
        digit = int(digit)
        total += digit

    return total
print(sum_of_digits(123))