def total_word_count(sentences):
    total = 0
    for sentence in sentences:
        words = sentence.split()
        count = len(words)
        total += count
    return total

print(total_word_count(["hello world", "how are you"]))