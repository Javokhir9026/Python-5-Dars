import os
os.system("cls")

def Tub_son_top(s: int):
    y = 0
    for i in range(1, s):
        if s % i == 0:
            y += i
    if y == s:
        print("Tub Son Emas!")
    else:
        print("Tub Son!")

n = int(input("N: "))
Tub_son_top(n)
