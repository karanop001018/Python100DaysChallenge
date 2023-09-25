# Getter
# class MyClass:
#     def __init__(self, value):
#         self._value = value

#     def show (self):
#         print(f'Value is {self._value}')

#     @property
#     def ten_value(self):
#         return 10 * self._value

# obj = MyClass(10)
# print(obj.ten_value)
# obj.show()

# ---------------------------------------------------------------------
# Setter

# class MyClass:
#     def __init__(self, value):
#         self._value = value
#
#     def show(self):
#         print(f'Value is {self._value}')
#
#     # Getter
#     @property
#     def ten_value(self):
#         return 10 * self._value
#
#     # Setter
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value / 10
#
#
# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()