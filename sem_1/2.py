nums = [i for i in range(1,11)]
squared = list(map(lambda x: x ** 2, nums))
cubic = list(map(lambda x: x ** 3, nums))
print(f'{nums} \n{list(squared)} \n{list(cubic)}')
print(*(list(filter(lambda x: x % 2 == 0, lst)) for lst in [nums, squared, cubic]))
