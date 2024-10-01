import os
os.system("cls")

def tekshir(ls):
    nls = []
    for i in ls:
        if i % 2 == 0:
            nls.append(i)
    return nls

ls = [1,2,3,4,5,6,7,8,9,10]
t = tekshir(ls)
print("Juftlari ==> ",t)