import string

def first_word(text):
    """ Пошук першого слова """
    b = 0
    c = 0
    for i in text:
        if i.isalpha():
            b = text.index(i)
            break
    c = b + 1
    for i in text[b+1:]:
        if (i in string.punctuation and i != "'") or i.isspace():
            break
        else:
            c += 1
    text = text[b:c]
    return text

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
