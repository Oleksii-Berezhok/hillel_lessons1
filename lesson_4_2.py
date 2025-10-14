lst = [0, 1, 7, 2, 4, 8]
if lst != []:
    lst_2 = sum(lst[::2])*lst[-1]
    print(lst_2)
else:
    print(lst)