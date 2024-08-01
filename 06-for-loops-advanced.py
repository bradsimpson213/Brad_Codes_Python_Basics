# FOR LOOPS ADVANCED

colors = ["red", "orange", "blue", "green", "purple"]


# for color in colors:
#     print(color)

# print(range(5))
# print(list(range(5)))
# range(start, end, step)
# print(list(range(0, 7)))
# print(list(range(10, 0, -1)))

# for index in range(len(colors)):
#     print(index, colors[index])

# print(enumerate(colors))
# print(list(enumerate(colors)))

for index, color in enumerate(colors, 1):
    print(index, color)