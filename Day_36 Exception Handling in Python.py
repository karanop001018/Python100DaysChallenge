a = input('Enter the number: ')
print(f'Multiplication table of {a} is:')
try:
    for i in range(1, 11):
        print(f'{int(a)} x {i} = {int(a) * i}')

except Exception as e:
    print('Sorry error occurred.')

print('End of program')

try:
    num = int(input('Enter an inter:'))
    a = [6, 3]
    print(a[num])
except ValueError:
    print('Number entered is not an integer.')
except IndexError:
    print('Index Error.')