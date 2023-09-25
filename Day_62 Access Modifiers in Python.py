# NOTE: There is no concept of public,private and protected. It is used     by people on name of public,private and protected.
# Types of access specifiers:
# (1) Public
# (2) Private
# (3) Protected


# PUBLIC ACCESS SPECIFIERS
# class Employee:
#     def __init__(self):
#         self.__name = 'Indian'

# a = Employee()
# # print(a.__name) #Cannot be accessed directly
# # Name Mangling
# print(a._Employee__name) # Can be accessed indirectly
# print(a.__dir__())


# class Student:
#     # constructor  defined
#     def __init__(self, age, name):
#         self.age = age               # public variable
#         self.name = name             # public variable

# obj = Student(18,"Karan")
# print(obj.age)
# print(obj.name)


# PRIVATE ACCESS SPECIFIERS
# class Student:
#     def __init__(self, age, name):
#         self.__age = age      # An indication of private variable

#     def __funName(self):  # An indication of private function
#         self.y = 34
#         print(self.y)

# class Subject(Student):
#     def __init__(self, age, name):
#         super().__init__(age, name)

# obj = Student(21,"Harry")
# obj1 = Subject(22, "Ron")

# # To access private attributes, you can use name mangling
# print(obj._Student__age)
# obj._Student__funName()

# # For the Subject class object, you can do the same
# print(obj1._Student__age)
# obj1._Student__funName()


# PROTECTED ACCESS SPECIFIERS
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):  # protected method
        return "CodeWithHarry"


class Subject(Student):  # inherited class
    pass


obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
