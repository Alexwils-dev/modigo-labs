def analyze_survey(responses):
    if not responses:
        return {"tally": {}, "most_popular": None}

    tally = {}

    for color in responses:
        if color not in tally:
            tally[color] = 0
        tally[color] += 1
            

    most_popular = None
    highest_count = 0
    
    for color, count in tally.items():
        if count > highest_count:
            highest_count = count
            most_popular = color

    return {"tally": tally, "most_popular": most_popular}
print(analyze_survey(["red", "blue", "red", "green"]))