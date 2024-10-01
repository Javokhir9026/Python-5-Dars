import os
os.system("cls")

def Taxtla(ls):
    lst = []
    for i in ls:
        if i != 0:
            lst.append(i)

    for j in ls:
        if j == 0:
            lst.append(j)
    return(lst)

lst = [1,0,2,0,3,4,5,0,7]
d = Taxtla(lst)
print(d)