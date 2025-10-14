from os import remove

lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
a = lst.count(0)
i = 0
while i < a:
    lst.remove(0)
    lst.append(0)
    i += 1
print(lst)
