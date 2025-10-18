import keyword
import string

name = input("Введіть рядок: ")

if not name:
    print(False)
elif name[0].isdigit():
    print(False)
elif name != name.lower():
    print(False)
elif " " in name:
    print(False)
elif "__" in name:
    print(False)
elif any(ch in string.punctuation and ch != "_" for ch in name):
    print(False)
elif keyword.iskeyword(name):
    print(False)
else:
    print(True)
