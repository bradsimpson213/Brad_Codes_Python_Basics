# VARIABLES

# brads_age = 123
# num_2 = 23.5

# dict_1 = {}

# tuple_1 = (1,)

# sorted_result = sorted(tuple_1)

# WEEK_DAYS = ("MON", "TUES", "WED", "THURS", "FRI")
# print(WEEK_DAYS)
# WEEK_DAYS = "Purple"
# print(WEEK_DAYS)

# SCOPE

num = 50
print("Global 1", num)
PI = 3.14

def my_function():
    # num = 30
    global num
    print("Local 1", num)
    num += 10
    print("Local 2", num)
    # if num > 40 :


my_function()

print("Global 2", num)
