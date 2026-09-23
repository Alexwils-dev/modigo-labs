def multiplication_table(number, limit):
    results = []

    for value in range(1, limit + 1):
        result = number * value
        results.append(result)

    return results

print(multiplication_table(3, 5))