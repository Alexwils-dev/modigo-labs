def path_hits_blocked(blocked, path):
    for position in path:
        if position in blocked:
            return True

    return False
print(path_hits_blocked({(1,1), (2,2)}, [(0,0), (1,1)]))