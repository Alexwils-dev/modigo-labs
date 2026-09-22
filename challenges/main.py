def build_countdown(start):
    countdown = []

    for number in range(start, 0, -1):
        countdown.append(number)

    return countdown

print(build_countdown(5))