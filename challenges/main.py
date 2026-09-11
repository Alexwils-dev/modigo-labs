def merge_tags(tags1, tags2):
    merged = tags1 | tags2
    return merged

print(merge_tags({"python", "web"}, {"web", "css"}))