def is_even(number: int) -> bool:
    text_str = str(number)
    if text_str[-1] in '2468':
        return True
    else:
        return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'