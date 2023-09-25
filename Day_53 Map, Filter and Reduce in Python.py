# def cube(x):
#     return x*x*x

# print(cube(2))

# l = [1,2,3,4,6,4,3]
# newl = []
# # NORMAL METHOD

# # for item in l:
# #     newl.append(cube(item))

# # Using MAP

# newl = list(map(cube,l))
# print(newl)

# newl = list(map(lambda x:x*x*x,l))
# print(newl)


# # FILTER
# def filter_function(a):
#     return a>3

# newnewl = filter(filter_function,l)
# print(newnewl)


# newnewl = list(filter(filter_function , l))
# print(newnewl)
















from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
# def sum(x,y):
#     return x+y
# sum = reduce(sum, numbers)
# OR
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)

