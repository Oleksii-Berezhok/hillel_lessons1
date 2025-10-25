def second_index(text, some_str):
    my_string = text
    x = my_string.count(some_str)
    if x > 1:
        b = my_string.find(some_str)
        c = my_string.find(some_str,b+1)
    else:
        c = None
    return c


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
