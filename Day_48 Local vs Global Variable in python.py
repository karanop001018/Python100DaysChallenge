x = 63 # Global variable
# print(x)

def hello():
    x = 36 # Local variable
    print(f"The local x is {x}")
    print('Hello Karan')


hello()
print(f"The global x is {x}")








x = 63 # Global variable
# print(x)

def hello():
    global x
    x = 36
    y = 9 #local variable
    print(f"The edited global x is {x}")
    print(f"This is local variable y: {y}")
    print('Hello Karan')

print(f"The original global x is {x}")
hello()
print(f"This will be edited global x: {x}")
# print(y) # It will give error as it is a local variable and not a global variable





