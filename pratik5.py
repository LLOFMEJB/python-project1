def absolute_value(value):
    if value < 0:
        return -value
    else:
        return value
value = int(input("write the value: "))
print(absolute_value(value))    