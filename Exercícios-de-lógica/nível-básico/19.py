import random
aluno1=str(input('Digite o nome do primeiro aluno: '))
aluno2=str(input('Digite o nome do segundo aluno: '))
aluno3=str(input('Digite o nome do terceiro aluno: '))
aluno4=str(input('Digite o nome do quarto aluno: '))

escolhido=random.choice([aluno1,aluno2,aluno3,aluno4])
print('O aluno/a escolhido foi o/a {:=^10}'.format(escolhido))