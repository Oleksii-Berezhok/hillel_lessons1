import math
l = [1, 2, 3, 4, 5]
x = math.ceil(len(l)/2)
a_list = l[:x]
b_list = l[x:]
new_list = [a_list,b_list]
print(new_list)