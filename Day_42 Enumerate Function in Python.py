marks = [12, 56, 32, 98, 12, 45, 1, 4]
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print('Karan, awesome!')
    index+=1


# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as list, tuple or string) and get the index and value of each element in the sequence of the same time.
marks = [12, 56, 32, 98, 12, 45, 1, 4]
for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print('Karan, awesome!')
    index += 1

