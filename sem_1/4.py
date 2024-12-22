def set_difference(set1, set2, set3, symmetric):
    if not symmetric:
        return set1 - set2 - set3
    else:
        return set1 ^ set2 ^ set3


set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {3, 4, 5, 6}
print(set_difference(set1, set2, set3, True))
