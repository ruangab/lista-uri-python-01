i = False
n1 = float('{:.1f}'.format(float(input("Digite o primeiro numero: "))))


while(i != True):
    if not (n1>=0 and n1<=10):
        n1 = float('{:.1f}'.format(float(input("Digite um numero de 0 a 10: "))))
    else:
        i = True

n2 = float('{:.1f}'.format(float(input("Digite o segundo numero: "))))
while(i != False):
    if not (n2>=0 and n2<=10):
        n2 = float('{:.1f}'.format(float(input("Digite um numero de 0 a 10: "))))
    else:
        i = False

n3 = float('{:.1f}'.format(float(input("Digite o terceiro numero: "))))
while(i != True):
    if not (n2>=0 and n2<=10):
        n3 = float('{:.1f}'.format(float(input("Digite um numero de 0 a 10: "))))
    else:
        i = True

media = ((n1*2)+(n2*3)+(n3*5))/10

print("MEDIA = {:.1f}".format(media))