def slicer(*num):
    even = []
    odd = []
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    print("even list : ", even)
    print("odd list : ", odd)
slicer(2,3,5,6,8,9,7,10,25)