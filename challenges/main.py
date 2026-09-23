def find_max(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
    return largest
print(find_max([3, 7, 2]))