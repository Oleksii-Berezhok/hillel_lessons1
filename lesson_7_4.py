
def common_elements():
        first_set = set(range (0,100, 3))
        second_set = set(range (0,100, 5))
        return first_set & second_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')