def top_words(text, n):
    if text == "":
        return []

    words = text.lower().split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    ranked_words = list(counts.items())
    ranked_words.sort(key=lambda item: (-item[1], item[0]))
    return ranked_words[:n]

print(top_words("the cat sat on the mat the cat ran", 2))