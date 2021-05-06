liste = [1, 2, 3, 4]
for i in liste:
    print(i, ":", (lambda x : "odd" if x%2 != 0 else "even") (i))
