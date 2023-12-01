def magic_calculation(a, b):
    if a < b:
        add = __import__('magic_calculation_102').add
        return add(a, b) + sum(range(4, 6))
    else:
        sub = __import__('magic_calculation_102').sub
        return sub(a, b)
