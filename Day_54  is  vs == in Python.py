a = [1,2,43]
b = [1,2,43]
print(a is b) # exact location of object in memory
print(a == b) # value
print('\n')


a = 3
b = 3
print(a is b) # exact location of object in memory
print(a == b) # value
print('\n')



a = (1,2)
b = (1,2)
print(a is b) # exact location of object in memory
print(a == b) # value
print('\n')



a = None
b = None
print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory
print(a == b) # value
