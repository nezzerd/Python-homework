def multiply_lists(list1, list2):
    return list(map(lambda x, y: x * y, list1, list2))

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]
print(multiply_lists(list1, list2))