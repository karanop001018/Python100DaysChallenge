# class Person:
#     name = 'Karan'
#     occupation = 'Data Scientist'
#     networth = 100

# a = Person()
# print(a.name, a.occupation)

# a.name = 'Krish'
# a.occupation = 'Web Developer'
# print(a.name, a.occupation)

# ----------------------------------------------------------------------

# class Person:
#     name = 'Karan'
#     occupation = 'Data Scientist'
#     networth = 100
#     def info(self):
#         print(f'{self.name} is a {self.occupation}')

# a = Person()
# a.info()


# ----------------------------------------------------------------------

# self : The object on which the method is called.

class Person:
    name = 'Karan'
    occupation = 'Data Scientist'
    networth = 100

    def info(self):
        print(f'{self.name} is a {self.occupation}')


a = Person()
b = Person()
c = Person()
a.name = 'Shubham'
a.occupation = 'Accountant'

b.name = 'Omkar'
b.occupation = 'HR'
a.info()
b.info()
c.info()  # if values of c is not given then it prints the default values

