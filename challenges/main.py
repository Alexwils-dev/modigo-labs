def count_items(items):
    counts = {}

    for item in items:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1

    return counts

print(count_items(["apple", "banana", "apple"]))