for i in range(5):
    print(i)
else:
    print('Sorry it over')

for i in range(6):
    print(i)
    if i == 4:
        break

else:
    print('Sorry it over')

# If the else content is printed then the loop is completed successfully
# But if it is not printed then the loop has break
