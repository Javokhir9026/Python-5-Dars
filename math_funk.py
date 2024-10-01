import math
import os
os.system("cls")

def katta(a:int,b:int):
    if a >= b:
        return a
    else:
        return b
    
k = katta(123,432)
print("Katta son ==> ",k)

k1 = max(123,321)
print("Katta son ==> ",k1)

f = math.factorial(int(input("son: ")))
print("Faktorial ==> ",f)

ls = [1,2,3,4,5]
s = sum(ls)
print(ls," Yigindisi ==> ",s)

def sum(a:int,b:int):
    return a+b
y = sum(12,21)
print("yigindi ==> ",y)

raqam = int(input("SON: "))

ab = abs(raqam)
print(ab)