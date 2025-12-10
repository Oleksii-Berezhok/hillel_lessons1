a = "Hello"
b = a.__iter__()
print(type(b)) # виведе  <class 'str_iterator'>
print(next(b))
print(next(b))
print(next(b))
a = (2, 4)
b = a.__iter__()
print(type(b)) # виведе <class 'tuple_iterator'>
print(b)  #  виведе <tuple_iterator object at 0x7f09dc3db760>
print(next(b))
print(b.__next__())

