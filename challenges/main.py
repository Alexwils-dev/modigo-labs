def list_average(numbers):
    if not numbers:
        return 0
    total = 0
    
    for num in numbers:
        total += num
    average = total / len(numbers)

    return round(average, 2)
print(list_average([2, 4, 6]))