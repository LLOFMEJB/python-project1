def absolute_value(value):
    """
    no negativity please
    """
    if value < 0:
        return -value
    else:
        return value
value = int(input("write the value: "))
print(absolute_value(value))
print(absolute_value.__doc__)