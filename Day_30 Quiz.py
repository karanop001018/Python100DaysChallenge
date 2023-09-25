'''
Write a program to print the Fibonacci sequence
f(0) = 1
f(1) = 1
f(2) = f(1) + f(0)
f(n) = f(n-1) + f(n-2)
'''


n = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto", n, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1