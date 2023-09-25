# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")

# class ChildClass(ParentClass):
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()


# class ParentClass1:
#     def parent_method(self):
#         print("This is the parent method of ParentClass1.")

# class ParentClass2:
#     def parent_method(self):
#         print("This is the parent method of ParentClass2.")

# class ChildClass(ParentClass1, ParentClass2):
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()


# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id


# class Programmer(Employee):
#   def __init__(self, name, id, lang):
#     super().__init__( name, id)
#     self.lang = lang

# Rohan = Employee("Rohan Das", "420")
# Karan = Programmer("Karan", "2345", "Python")
# print(Karan.name)
# print(Karan.id)
# print(Karan.lang)





