def filter_and_group(catalog, required_tags, excluded_tags):
    result = {}

    for product in catalog:
        tags = product["tags"]

        if not required_tags.issubset(tags):
            continue

        if excluded_tags.intersection(tags):
            continue

        category = product["category"]
        name = product["name"]

        if category not in result:
            result[category] = []

        result[category].append(name)
    return result