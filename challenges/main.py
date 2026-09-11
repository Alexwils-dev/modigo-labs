def compare_hobbies(person1_hobbies, person2_hobbies):
    return {
        "shared": person1_hobbies & person2_hobbies,
        "only_person1": person1_hobbies - person2_hobbies,
        "only_person2": person2_hobbies - person1_hobbies
    }

print((["reading", "coding"]))