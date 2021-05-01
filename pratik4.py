def calculate(a, b, c):
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "/":
        print(a/b)
    elif c == "*":
        print(a*b)
    elif c == "%":
        print(a%b)
    elif c == "//":
        print(a//b)
    else:
        print("Enter a valid operator!")
calculate(21,3,"/")