import os
os.system("cls")

def Aniqla(sonlar):
    tub_sonlar = []
    for j in sonlar:
        if j > 1:
            t = 1 
        for i in range(2, int(j**0.5) + 1):
            if j % i == 0:
                t = 0
                break
        if t == 1:
            tub_sonlar.append(j)
    return

sonlar = [1,2,3,4,5,6,7,8]
q = Aniqla(sonlar)
print(q)
