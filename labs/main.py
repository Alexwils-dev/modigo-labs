def pair_names_and_ages(names, ages):
    result = {}

    for name, age in zip(names, ages):
        result[name] = age

    return result
print(pair_names_and_ages(["Ada", "Bola"], [25, 30]))