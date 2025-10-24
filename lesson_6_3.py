number = str(input("Введіть ціле число:"))

while int(number) > 9:
    c = 1
    a = len(number)
    for i in range(a):
        b = int(number[i])
        c *= b
    number = str(c)

print(number)