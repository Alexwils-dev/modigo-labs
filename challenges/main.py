def total_scores(rounds):
    totals = {}
    for round_scores in rounds:
        for player, points in round_scores.items():
            if player not in totals:
                totals[player] = 0

            totals[player] += points
    return totals

print(total_scores([{"Ada": 5, "Bola": 3}, {"Ada": 2, "Bola": 4}]))