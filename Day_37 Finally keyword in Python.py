'''
Use of finally:--
--->The finally keyword is used in try...except blocks. It defines a block of code to run when the try...except...else block is final.

--->The finally block will be executed no matter if the try block raises an error or not.

--->This can be useful to close objects and clean up resources.
'''


# try:
#     l = [1,5,6,7]
#     i = int(input('Enter the index'))
#     print(l[i])
# except:
#     print('Some error occurred')
# finally:
#     print('I am always executed either input is valid or not')


def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input('Enter the index'))
        print(l[i])
        return 1
    except:
        print('Some error occurred')
        return 0
    finally:
        print('I am always executed either input is valid or not')


x = func1()
print(x)


