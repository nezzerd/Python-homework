def superset(set1, set2):
    if set1 == set2:
        return 3
    elif set1 < set2 or set2 < set1:
        return 2
    else:
        return 1


set1 = {1, 2, 3}
set2 = {1, 2}

print(superset(set1, set2))
