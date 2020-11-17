nota = int(input())

valores = [100, 50, 20, 10, 5, 2, 1]
print(nota)
for x in valores:
    print(str(nota//x) +  " nota(s) de R$ {},00".format(x))
    nota %= x
