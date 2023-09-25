# Two types of constructors: (I) Parameterised Constructors
                           # (II) Default Constructors: If there are no arguments given


# class Person():
#     name = 'Karan'
#     occ = 'Developer'
#     def info(self):
#         print(f'{self.name} is a {self.occ}')

# a = Person()
# b = Person()
# a.name = 'Diya'
# a.occ = 'HR'
# a.info()
# b.info()

# ----------------------------------------------------------------------

class Person():
    def __init__(self, name, occ):
        print('Hey I am a person')
        self.name = name
        self.occ = occ

    def info(self):
        print(f'{self.name} is a {self.occ}')


a = Person('Karan',
           'Developer')  # Here 3 arguments are passed (saelf,n,o) self is passed automatically, n & o are passed by us.
b = Person('Diya', 'HR')
# a.name = 'Diya'
# a.occ = 'HR'
a.info()
b.info()

