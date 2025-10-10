a = int(input("Будь ласка введіть пятизначне число:"))
b = a//10000
c = a%10000//1000
d = a%1000//100
e = a%100//10
f = a%10
print(str(f) + str(e) + str(d) + str(c) + str(b))

