from functools import reduce


def get_sum(nums):
    return reduce(lambda x, y: x + y, nums)


nums = [i for i in range(1, 10001)]
print(get_sum(nums))
