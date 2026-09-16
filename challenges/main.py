def find_longest_word(words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
print(find_longest_word(["same", "size"]))