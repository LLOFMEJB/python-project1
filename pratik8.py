def slicer(*num):
    print("even list : ", [i for i in num if i%2 == 0])
    print("odd list : ", [i for i in num if i%2 == 1])
slicer(2,3,5,6,8,9,7,10,25)