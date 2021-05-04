"""
Challenge - 2: Calculate Stock Profit
"""
def karımne(fiyatlar):
    fiyatlar.sort()
    max_kar = (fiyatlar[len(fiyatlar)-1])-(fiyatlar[0])
    print(f"yapılabilecek max kar {max_kar} tl olacaktır.")
karımne([150,65,140,60,100,120,130])