def strvalid(s):
    par_grup = {"(":")", "[":"]", "{":"}"}
    open_par = ["(","[","{"]
    kontrol = []
    for i in s:
        if i in open_par:
            kontrol.append(i)
        elif kontrol and i == par_grup[kontrol[-1]]:
            kontrol.pop()
        else:
            return False
    return stack == []
kontrol_girdi = input("Sadece `(`, `)`, `{`, `}`, `[`, `]' elemanlarından oluşan kurallı bir girdi yapınız:")
print strvalid(kontrol_girdi)