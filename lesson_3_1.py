a = int(input("Введіть перше число:"))
b = int(input("Введіть друге число:"))
c = input("Введіть математичну дію (+, - , *, /):")
if c == "+" :
    print (a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
else:
    print(a/b)
