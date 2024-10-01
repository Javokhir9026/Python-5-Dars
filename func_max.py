import os
os.system("cls")

def qimmat_aniqla(dic : dict):
    narxi = list(dic.values())
    qimmat = max(narxi)
    for i in dic:
        if dic[i] == qimmat:
            return {i : dic[i]}

mahsulot = {"kartoshka": 7000, "sabzi": 12000, "piyoz": 3000}
q = qimmat_aniqla(mahsulot)
print(q)