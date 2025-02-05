from math import radians, sin, cos, tan
angulo=int(input("Digite o valor angulo: "))
radianos=radians(angulo)
seno=sin(radianos)
cosseno=cos(radianos)
tangente=tan(radianos)
print('O seno do angulo {}° vale {:.1f}'.format(angulo, seno))
print('O cosseno do angulo {}° vale {:.1f}'.format(angulo, cosseno))
print('A tangente do angulo {}° vale {:.1f}'.format(angulo, tangente))