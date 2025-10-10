first_lst = [5, 9, [9,1,3], True, False]
if first_lst == []:
    print(first_lst)
else:
    a = first_lst.pop()
    first_lst.insert(0,a)
    print(first_lst)