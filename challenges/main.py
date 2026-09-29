def can_make_recipe(pantry, recipe, substitutes):
    for ingredient, required_quantity in recipe.items():
        satisfied = False

        if ingredient in pantry and pantry[ingredient] >= required_quantity:
            satisfied = True

        else:
            possible_substitutes = substitutes.get(ingredient, set())

            for substitute in possible_substitutes:
                if substitute in pantry and pantry[substitute] >= required_quantity:
                    satisfied = True
                    break

        if not satisfied:
            return False

    return True

print(can_make_recipe({"flour": 2, "sugar": 1}, {"flour": 1, "sugar": 1}, {}))