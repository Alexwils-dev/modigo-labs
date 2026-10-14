def shared_hobbies(hobbies1, hobbies2):
    return set(hobbies1) & set(hobbies2)

print(shared_hobbies(["reading", "chess"], ["chess", "cooking"]))
print(shared_hobbies(["reading"], ["cooking"]))