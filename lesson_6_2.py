seconds = int(input("Введіть секунди від 0 до 8640000:"))
days,x = divmod(seconds,86400)
hours,y = divmod(x,3600)
mins,seconds = divmod(y,60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"


print(f"{days} {day_word} , {str(hours).zfill(2)} : {str(mins).zfill(2)} : {str(seconds).zfill(2)}")