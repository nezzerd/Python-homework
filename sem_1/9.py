def list_to_set(nums):
    set_nums = set()
    for i in range(len(nums)):
        if not nums[i] in set_nums:
            set_nums.add(nums[i])
        else:
            count = nums[:i + 1].count(nums[i])
            set_nums.add(int(str(nums[i]) * count))
    return set_nums


list = [1, 1, 1, 2, 2, 2, 3, 3]
print(list_to_set(list))
