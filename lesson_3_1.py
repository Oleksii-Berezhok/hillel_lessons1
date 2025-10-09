a = int(input("Введіть перше число:"))
b = int(input("Введіть друге число:"))
if b != 0:
    c = input("Введіть математичну дію (+, - , *, /):")
    if c == "+" :
        print (a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        print(a / b)
    elif c == 0 :
        print("Не можна ")
    else:
        print("Ви ввели не вірну дію")
else:
    print("На ноль не можна ділити")