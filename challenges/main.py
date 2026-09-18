def has_conflict(meetings):
    meetings.sort(key=lambda meeting: meeting[0])
    
    for i in range(len(meetings) - 1):
        current_start, current_end = meetings[i]
        next_start, next_end = meetings[i + 1]

        if current_end > next_start:
            return True

    return False

print(has_conflict([(1, 3), (2, 4)]))
print(has_conflict([(1, 3), (3, 5)]))