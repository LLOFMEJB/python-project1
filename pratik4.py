def calculate(a, b, c):
    if c == "+":
        return (a+b)
    elif c == "-":
        return (a-b)
    elif c == "/":
        return (a/b)
    elif c == "*":
        return (a*b)
    elif c == "%":
        return (a%b)
    elif c == "//":
        return (a//b)
    else:
        return ("Enter a valid operator!")
print(calculate(21,3,"/"))