# Day52

# def double(x):
#     return x*2

double = lambda x: x * 2
# square = lambda x:x*x
cube = lambda x: x * x * x
print(double(5))
# print(square(5))
print(cube(5))
# print(double(6), square(6), cube(6))


avg = lambda x, y, z: (x + y + z) / 3  # use lambda function only when you are asked to complete code in one line
print(avg(3, 5, 10))


def appl(fx, value):
    return 6 + fx(value)


print(appl(lambda x: x * x, 2))
print(appl(cube, 2))  # fx(value) = cube of 2

