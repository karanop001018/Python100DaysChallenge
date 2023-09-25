dic = {63: 'Karan', 36: 'Diya', 96: 'Omkar', 10: 'Ami'}
'''
Here, in the dictionary given above 
63,36,96,10 are the keys & 
'Karan', 'Diya','Omkar','Ami' are the values of their respective keys
'''
print(dic)
print(dic[63])
print(dic.get(36))  # prints the values in given key
print(dic.keys())  # key() prints all the keys of the dictionary
print(dic.values())  # values() prints all the values of their respective keys

for key in dic.keys():
    print(f'\nThe enrollment number {key} is of {dic[key]}')

for key in dic.keys():
    print('\n', dic.values())

print(dic.items())
for key, value in dic.items():
    print(f'The value corresponding to the key {key} is {value}')

# make a program of your class students giving first year cgpa