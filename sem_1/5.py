def delete_odds(nums):
    return list(filter(lambda x: x % 2 == 0, nums))

nums = [1, 2, 3, 4, 5]
print(delete_odds(nums))