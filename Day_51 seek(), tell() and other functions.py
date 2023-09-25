# with open('kp3.txt', 'r') as f:
#     print(type(f))
#     # Move to the 10th byte in the file.
#     f.seek(10)  # seek(10) reads the file from 10th character
#     # Ex: 1,2,3,4,5,6,7,8,9,10,11
#     # prints 6(if considers ',') as output
#     # Read the next 5 byte.
#     print(f.tell())
#     data = f.read(5)
#     print(data)

with open('kp4.txt', 'w') as f:
    f.write('Hello World')
    f.truncate(5)  # prints element upto 5 means size of file is 5 bytes so prints 'Hello'
