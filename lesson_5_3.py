import string

name = input("Введіть рядок: ")
name = name.title()
name = name.replace(" ", "")

for ch in name:
    if ch in string.punctuation:
        name = name.replace( ch, "")
name = "#" + name
if len(name) > 140:
    name = name[:140]
print(name)
