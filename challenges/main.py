def find_index(numbers, target):
    if not numbers:
        return -1

    left = 0
    right = len(numbers) -1

    while left <= right:
        middle_index = (left + right) // 2
        middle_value = numbers[middle_index]

        if middle_value == target:
            return middle_index

        if middle_value < target:
            left = middle_index + 1
        else:
            right = middle_index - 1
    return -1



print(find_index([1, 3, 5, 7, 9], 5))