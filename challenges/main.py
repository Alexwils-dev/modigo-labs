def analyze_sales(prices):
    total = 0
    highest = prices[0]
    lowest = prices[0]

    for price in prices:
        total += price

        if price > highest:
            highest = price

        if price < lowest:
            lowest = price

    average = round(total / len(prices), 2)

    return {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest
    }

print(analyze_sales([500, 1200, 300]))