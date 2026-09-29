def all_unique_tags(posts):
    unique_tags = set()
    for post in posts:
        for tag in post["tags"]:
            unique_tags.add(tag)

    return unique_tags