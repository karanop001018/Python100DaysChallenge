ep1 = {122:45, 123:89, 567:69, 670:69}
ep2 = {222:67, 566:90}
ep1.update(ep2)
print(ep1)
ep1.clear() # It empty the given dictionary
print(ep1)

ep1 = {122:45, 123:89, 567:69, 670:69}
ep1.pop(123) #pop/delete the given value
print(ep1)

ep1 = {122:45, 123:89, 567:69, 670:69}
ep1.popitem() #deletes the last elementof the dictionary
print(ep1)

# ep1 = {122:45, 123:89, 567:69, 670:69}
# del ep1  #deletes the dictionary and if we try to print that dictionary we will get error because it has been deleted already
# print(ep1)


ep1 = {122:45, 123:89, 567:69, 670:69}
del ep1[122]
print(ep1)

