first_lst = [2,1,3]
if first_lst == []:
    print(first_lst)
else:
    a = first_lst[0]
    b = first_lst[-1]
    first_lst[0] = b
    first_lst[-1] = a
    print(first_lst)