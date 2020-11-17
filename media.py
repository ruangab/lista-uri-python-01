i = False
n1 = float('{:.1f}'.format(float(input("Digite o primeiro número: "))))
print (str(n1))

while(i != True):
    if not (n1>=0 and n1<=10):
        n1 = float('{:.1f}'.format(float(input("Digite um número de 0 a 10: "))))
    else:
        i = True

n2 = float('{:.1f}'.format(float(input("Digite o segundo número: "))))
while(i != False):
    if not (n2>=0 and n2<=10):
        n2 = float('{:.1f}'.format(float(input("Digite um número de 0 a 10: "))))
    else:
        i = False


media = ((n1*3.5)+(n2*7.5))/11

print("MEDIA =  {:.5f}".format(media))