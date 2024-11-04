# List Comprehensions

nums = [ 1, 3, 4, 5, 7, 8, 9, 10, 12, 15, 18, 21, 24]

nums_copy = []
for num in nums:
    nums_copy.append(num)


# print(nums_copy)
# nums_lc_copy = [ num for num in nums]
# print(nums_lc_copy)

# mapped_nums = map(lambda num: num * 2, nums)
# print(mapped_nums)
# print(list(mapped_nums))
# mapped_nums_lc = [num * 2 for num in nums]
# print(tuple(mapped_nums_lc))
# nums_filter = filter(lambda num: num % 2 == 0, nums)
# print(list(nums_filter))
# nums_filter_lc = [ num for num in nums if num % 2 == 0]
# print(nums_filter_lc)

nums_filter_and_map_lc = [ num * 2 for num in nums if num % 2 == 0]
print(nums_filter_and_map_lc)