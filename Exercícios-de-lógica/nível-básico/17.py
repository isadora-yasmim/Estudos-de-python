from math import pow, sqrt
co=float(input("Digite o valor do cateto oposto: "))
ca=float(input("Digite o valor do cateto adjacente: "))
h=sqrt(pow(co,2)+pow(ca,2))
print('O valor da hipotenusa desse triangulo e {:.2f}' .format(h))