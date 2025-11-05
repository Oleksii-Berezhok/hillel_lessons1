def pow(x:int):
    return x ** 2

def some_gen(begin:int, end:int, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    i = begin
    def increment():
        count = 0
        nonlocal i
        while count < end:
            yield i
            i = func(i)
            count += 1
    return increment()


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
