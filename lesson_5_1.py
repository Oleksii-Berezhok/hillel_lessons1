import keyword
import string

str1 = str(input("Введіть рядок: "))
if (not str1[0].isdigit()
    and str1 == str1.lower()
    and str1.count("_") <= 1
    and " " not in str1
    and not any(char in string.punctuation and char != "_" for char in str1)
    and not keyword.iskeyword(str1)
    ):
    print(True)
else:
    print(False)