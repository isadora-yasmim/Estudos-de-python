altura=float(input("Digite a altura da parede em metros: "))
largura=float(input("Digite a largura da parede em metros: "))
area = altura * largura
tinta = area / 2
print('Para pintar essa parede voce gastara {:.1f} litros de tinta, ja que ela tem {:.2f} metros quadrados.'.format(tinta, area))
