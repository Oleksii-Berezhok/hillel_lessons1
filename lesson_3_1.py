a = int(input("Введіть перше число:"))
b = int(input("Введіть друге число:"))
c = input("Введіть математичну дію (+, - , *, /):")
if c == "+" :
    print (a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("Помилка: не можна ділити на нуль!")
else:
    print("Ви ввели не вірну дію")
