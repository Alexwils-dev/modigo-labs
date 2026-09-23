def count_character(text, target):
    count = 0

    for char in text:
        if char == target:
            count += 1
    return count

print(count_character("banana", "a"))