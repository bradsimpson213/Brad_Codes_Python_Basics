





f = open("words.txt", "r")
print(list(f))

# OPEN Built In Function






















# Python Ternary Syntax

# party = False

# fun = "Oh yeah! 😆" if party else "Booo 😢"

# print(fun)

# print("Oh yeah! 😆" if party else "Booo 😢")













# BUILT INS ANY & ALL
# nums = [1, 2, 3]
# print("ANY", any(nums))
# print("ALL", all(nums))

# misc_vals = [False, 0, None]
# print("ANY", any(misc_vals))
# print("ALL", all(misc_vals))

# more_vals = [0, "B"]
# print("ANY", any(more_vals))
# print("ALL", all(more_vals))

# empty = []
# print("ANY", any(empty))
# print("ALL", all(empty))

# ANY needs 1 True value
# ALL needs 0 False values







# # BUILT INS MATHY STUFF SUM MIN MAX

# nums_list = [1, 2, 3, 4, 5]
# nums_tuple = (2, 4, 6, 8, 10)
# nums_set = {1, 3, 5, 7, 9}

# print("SUM:", sum(nums_list))
# print("MIN:", min(nums_tuple))
# print("MAX:", max(nums_set))

# letters_list = ['a', 'b', 'c', 'd', 'e']
# print("MIN:", min(letters_list))
# print("MAX:", max(letters_list))
# print("SUM???", sum(letters_list))

















# BUILT IN MAP FUNCTION

# nums = [1, 2, 3, 4, 6, 7, 8]

# doubled = map(lambda num: num * 2, nums)

# print(doubled)
# print("Doubled", list(doubled))

# def halved(num):
#     return num / 2

# halved_vals = map(halved, nums)

# print("Halved", list(halved_vals))










# BUILT IN INPUT FUNCTION


# name = input("Whats your name? ")

# print(f"Your name is {name}!")

# print(type(name) == str)





















# BUILT IN FILTER FUNCTION

# nums = [1, 2, 3, 4, 6, 7, 8]

# evens = filter(lambda num: num % 2 == 0, nums)

# print(evens)
# print("Evens:", list(evens))

# def is_odd(num):
#     return num % 2 != 0

# odds = filter(is_odd, nums)

# print("Odds:", list(odds))



# BUILT IN ZIP FUNCTION

# names = ["Tom", "Mike", "Ned"]
# ages = [23, 26, 24, 31] 

# zipped_names_ages = zip(names, ages)
# # print(zipped_names_ages)
# # print(list(zipped_names_ages))

# name_age_dict = dict(zipped_names_ages)
# print(name_age_dict)


# BUILT IN ROUND FUNCTION

# num = 1.26
# other_num = 3.12345
# yet_another_num = 350

# print(round(num, 1))
# print(round(other_num, 2))
# print(round(yet_another_num, -2))


# BUILT IN SORTED FUNCTION

# colors = ["red", "Orange", "blue", "green"]
# more_colors = ("purple", "yellow", "brown")
# even_more_colors = {"pink", "khaki"}

# sorted_colors = sorted(colors, key=lambda color: color.lower())
# sorted_more_colors = sorted(more_colors)
# sorted_even_more_colors = sorted(even_more_colors)

# print("colors", sorted_colors)
# print("more_colors", tuple(sorted_more_colors))
# print("even_more_colors", set(sorted_even_more_colors))