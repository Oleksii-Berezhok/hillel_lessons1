import string

letters = str(input("Введіть дві букви через дифіз: "))
lst = letters.split("-")
first = str(lst[0])
second = str(lst[1])
c = string.ascii_letters
a =c.find(first)
b = c.find(second)
d = c[a:b+1]
print(d)