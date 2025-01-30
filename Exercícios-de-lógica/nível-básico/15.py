km=float(input('Digite o numero de KMs percorridos:'))
dias=int(input('Digite a quantidade de dias em que usou o carro:'))
aluguel=(60*dias)+(km*0.15)
print('O valor do aluguel do carro ficou {:.2f} reais'.format(aluguel))